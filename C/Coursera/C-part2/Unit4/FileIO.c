#include <stdio.h>

// use C-part-1/Unit3/AvgWeights.c as reference
// helpful link https://www.tutorialspoint.com/cprogramming/c_file_io.htm

void printFile(FILE *fptr)
{
    int c;
    rewind(fptr);
    while ((c = getc(fptr)) != EOF)
        putc(c, stdout);
}

void doubleSpace(FILE *ifp, FILE *ofp)
{
    int c;
    rewind(ifp);
    while ((c = getc(ifp)) != EOF)
    {
        putc(c, ofp);
        // putchar(c);
        if (c == '\n')
            putc('\n', ofp);
    }
}

int main(int argc, char *argv[])
{
    FILE *fptr = fopen("MyFile.txt", "w"); // open file to write
    // do stuff
    fclose(fptr); // close file
    printf("%%d");
    return 0;
}