/*
 * Copyright 1993-2010 NVIDIA Corporation.  All rights reserved.
 *
 * NVIDIA Corporation and its licensors retain all intellectual property and 
 * proprietary rights in and to this software and related documentation. 
 * Any use, reproduction, disclosure, or distribution of this software 
 * and related documentation without an express license agreement from
 * NVIDIA Corporation is strictly prohibited.
 *
 * Please refer to the applicable NVIDIA end user license agreement (EULA) 
 * associated with this source code for terms and conditions that govern 
 * your use of this NVIDIA software.
 * 
 */

#include "../common/book.h"

#define sum_squares(x)  (x*(x+1)*(2*x+1)/6)

const int N = 10;
const int threadsPerBlock = 256;
const int blocksPerGrid = min(32, (N + threadsPerBlock - 1) / threadsPerBlock);

__global__ void dot(float *a, float *b, float *c) {
    __shared__ float cache[threadsPerBlock];
    int tid = threadIdx.x + blockIdx.x * blockDim.x;
    int cacheIndex = threadIdx.x;

    float sum = 0;
    while (tid < N) {
        sum += a[tid] * b[tid];
        tid += blockDim.x * gridDim.x;
    }

    cache[cacheIndex] = sum;

    __syncthreads(); // sync threads in current block (shared mem is stored at block level)

    // log reduction of array - wicked cool and fast
    // threadsPerBlock needs to be a power of 2 for this
    // ? maybe it doesn't NEED to be if this is revised?
    int i = blockDim.x / 2;
    while(i != 0) {
        if(cacheIndex < i) {
            cache[cacheIndex] += cache[cacheIndex + i];
        }
        __syncthreads();
        i /= 2;
    }

    if (cacheIndex == 0) {
        c[blockIdx.x] = cache[0];
    }
}

int main(void) {
    float *a, *b, c, *partial_c;
    float *dev_a, *dev_b, *dev_partial_c;

    // allocate CPU memory
    a = (float *) malloc(N*sizeof(float));
    b = (float *) malloc(N*sizeof(float));
    partial_c = (float *) malloc(blocksPerGrid * sizeof(float));

    // allocate GPU memory
    HANDLE_ERROR(cudaMalloc((void **) &dev_a, N * sizeof(float)));
    HANDLE_ERROR(cudaMalloc((void **) &dev_b, N * sizeof(float)));
    HANDLE_ERROR(cudaMalloc((void **) &dev_partial_c, blocksPerGrid * sizeof(float)));

    // fill CPU variables with values
    for(int i = 0; i < N; i++) {
        a[i] = i;
        b[i] = i;
    }

    // copy variable data from CPU to allocated memory on GPU
    HANDLE_ERROR(cudaMemcpy(dev_a, a, N * sizeof(float), cudaMemcpyHostToDevice));
    HANDLE_ERROR(cudaMemcpy(dev_b, b, N * sizeof(float), cudaMemcpyHostToDevice));

    // do the dot product computation on the GPU kernel
    dot<<<blocksPerGrid, threadsPerBlock>>>(dev_a, dev_b, dev_partial_c);

    // copy results back over to the CPU
    HANDLE_ERROR(cudaMemcpy(partial_c, dev_partial_c, blocksPerGrid * sizeof(float), cudaMemcpyDeviceToHost));

    // verify results
    c = 0;
    for(int i = 0; i < blocksPerGrid; i++) {
        c += partial_c[i];
    }

    // printf( "Does GPU value %.6g = %.6g?\n", c, 2 * sum_squares( (float)(N - 1) ) );
    printf("GPU gets %0.6g\n", c);
    printf("CPU gets %0.6g\n", sum_squares((float) (N-1)));

    // free GPU memory
    cudaFree(dev_a);
    cudaFree(dev_b);
    cudaFree(dev_partial_c);

    // free CPU memory
    free(a);
    free(b);
    free(partial_c);
}