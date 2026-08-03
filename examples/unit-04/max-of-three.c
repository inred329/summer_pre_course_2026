#include <stdio.h>

int max_of_three(int a, int b, int c) {
    int max = a;

    if (b > max) {
        max = b;
    }
    if (c > max) {
        max = c;
    }

    return max;
}

int main(void) {
    int a;
    int b;
    int c;

    if (scanf("%d %d %d", &a, &b, &c) != 3) {
        printf("Invalid input\n");
        return 1;
    }

    printf("Max: %d\n", max_of_three(a, b, c));
    return 0;
}
