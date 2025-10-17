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

#define N (33*1024)

__global__ void add(int *a, int *b, int *c) {
    int tid = threadIdx.x + blockIdx.x * blockDim.x;
    while(tid < N) {
        c[tid] = a[tid] + b[tid];
        tid += blockDim.x * gridDim.x;
    }
}

int main(void) {
    int a[N], b[N], c[N];
    int *dev1, *dev2, *dev3;

    HANDLE_ERROR(cudaMalloc((void**) &dev1, N*sizeof(int)));
    HANDLE_ERROR(cudaMalloc((void**) &dev2, N*sizeof(int)));
    HANDLE_ERROR(cudaMalloc((void**) &dev3, N*sizeof(int)));

    for(int i = 0; i < N; i++) {
        a[i] = -i;
        b[i] = i;
    }

    HANDLE_ERROR(cudaMemcpy(dev1, a, N*sizeof(int), cudaMemcpyHostToDevice));
    HANDLE_ERROR(cudaMemcpy(dev2, b, N*sizeof(int), cudaMemcpyHostToDevice));

    add<<<128,128>>>(dev1, dev2, dev3);

    HANDLE_ERROR(cudaMemcpy(c, dev3, N*sizeof(int), cudaMemcpyDeviceToHost));

    for(int i = 0; i < N; i++) {
        if((a[i] + b[i]) != c[i]) {
            printf("Error: %d + %d != %d", a[i], b[i], c[i]);
        } else {
            printf("%d + %d = %d\n", a[i], b[i], c[i]);
        }
    }   

    cudaFree(dev1);
    cudaFree(dev2);
    cudaFree(dev3);

    return 0;    
}