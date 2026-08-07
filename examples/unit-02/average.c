#include <stdio.h>

int main(void) {
    int total;
    int count;

    if (scanf("%d %d", &total, &count) != 2) {
        printf("Invalid input\n");
        return 1;
    }

    if (count <= 0) {
        printf("Count must be positive\n");
        return 1;
    }

    double average = (double) total / count;
    printf("Average: %.2f\n", average);
    return 0;
}
