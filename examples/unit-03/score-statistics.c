#include <stdio.h>

int main(void) {
    int score;
    int count = 0;
    int sum = 0;

    while (scanf("%d", &score) == 1 && score != -1) {
        if (score >= 0 && score <= 100) {
            count++;
            sum += score;
        }
    }

    if (count == 0) {
        printf("No valid score\n");
    } else {
        printf("Count: %d\n", count);
        printf("Sum: %d\n", sum);
        printf("Average: %.2f\n", (double) sum / count);
    }

    return 0;
}
