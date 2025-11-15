# CUDA

This is my attempt at learning CUDA from the book [CUDA By Example](https://edoras.sdsu.edu/~mthomas/docs/cuda/cuda_by_example.book.pdf).

All code here is code that I have replicated from the book for my own understanding, as well as any additional programs I write to better understand CUDA.

## Cool/Helpful links:
- https://cuda-tutorial.readthedocs.io/en/latest/tutorials/tutorial01/
- https://developer.nvidia.com/cuda-example

## Compiling and running

Compile with `nvcc <filename>`

Generates 3 files (by default):
- `a.exe` run this file
- `a.exp`
- `a.lib`

Handy compiler flags:
- `-o` specify name of output file
- `-odir` specify name of output directory
- `-I` include path
- `-g` host/CPU debug
- `-G` device/GPU debug