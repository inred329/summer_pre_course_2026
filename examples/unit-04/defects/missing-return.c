#include <stdio.h>

int max_of_three(int a, int b, int c) {
    int max = a;

    if (b > max) {
        max = b;
    }
    if (c > max) {
        max = c;
    }

    /* Defect: missing return statement for a non-void function. */
}

int main(void) {
    printf("Max: %d\n", max_of_three(3, 8, 5));
    return 0;
}
