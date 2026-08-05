#include <stdio.h>
int main(void) { int score; if (scanf("%d", &score) != 1) { puts("Invalid input"); return 1; } printf("Adjusted score: %d\n", score + 5); return 0; }
