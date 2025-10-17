#include <stdio.h>
#define NDEBUG //! must come before <assert.h>
#include <assert.h>
#include <ctype.h>

int main()
{
    // assert fails when NDEBUG is not defined
    // assert(0);
    // printf("Won\'t get printed, assertion above will fail");

    assert(0);
    printf("My program runs\n");
    return 0;
}
