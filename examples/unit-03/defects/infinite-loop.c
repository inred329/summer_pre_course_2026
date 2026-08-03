#include <stdio.h>

int main(void) {
    int value = 0;

    while (value < 5) {
        printf("%d\n", value);
        /* Defect: value is never updated, so the loop does not terminate. */
    }

    return 0;
}
