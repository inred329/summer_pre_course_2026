#include <stdio.h>

int main(void) {
    int total;
    int count;

    if (scanf("%d %d", &total, &count) != 2 || count == 0) {
        printf("Invalid input\n");
        return 1;
    }

    double average = (double) total / count;
    printf("Average: %.1f\n", average);
    return 0;
}
