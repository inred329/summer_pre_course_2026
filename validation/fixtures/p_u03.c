#include <stdio.h>
int main(void) { int score; if (scanf("%d", &score) != 1) { puts("Invalid input"); return 1; } puts(score >= 60 ? "Pass" : "Try again"); return 0; }
