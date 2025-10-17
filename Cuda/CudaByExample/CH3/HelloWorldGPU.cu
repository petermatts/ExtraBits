#include "../common/book.h"

__global__ void hello()
{
    printf("Hello world from GPU!\n");
}

int main()
{
    hello<<<1,1>>>();
    return 0;
}