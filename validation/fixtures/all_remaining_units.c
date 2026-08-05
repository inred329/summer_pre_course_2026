#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[20];
    int id;
    double average;
} Student;

static int add_bonus(int score, int bonus, int *result) {
    if (result == NULL) return 0;
    if ((bonus > 0 && score > INT_MAX - bonus) ||
        (bonus < 0 && score < INT_MIN - bonus)) return 0;
    *result = score + bonus;
    return 1;
}

static int max_array(const int values[], int length, int *result) {
    if (values == NULL || result == NULL || length <= 0) return 0;
    int maximum = values[0];
    for (int i = 1; i < length; ++i) {
        if (values[i] > maximum) maximum = values[i];
    }
    *result = maximum;
    return 1;
}

static int factorial_checked(int n, unsigned long long *result) {
    if (result == NULL || n < 0) return 0;
    if (n <= 1) { *result = 1; return 1; }
    unsigned long long smaller;
    if (!factorial_checked(n - 1, &smaller)) return 0;
    if (smaller > ULLONG_MAX / (unsigned long long)n) return 0;
    *result = smaller * (unsigned long long)n;
    return 1;
}

static int swap_values(int *a, int *b) {
    if (a == NULL || b == NULL) return 0;
    int temporary = *a;
    *a = *b;
    *b = temporary;
    return 1;
}

static int set_name(Student *student, const char *name) {
    if (student == NULL || name == NULL) return 0;
    int written = snprintf(student->name, sizeof student->name, "%s", name);
    if (written < 0 || (size_t)written >= sizeof student->name) {
        student->name[0] = '\0';
        return 0;
    }
    return 1;
}

static int calculate_average(const int values[], int length, double *average) {
    if (values == NULL || average == NULL || length <= 0) return 0;
    long long sum = 0;
    for (int i = 0; i < length; ++i) sum += values[i];
    *average = (double)sum / length;
    return 1;
}

static bool is_valid_score(int score) {
    return score >= 0 && score <= 100;
}

int main(void) {
    int adjusted;
    if (!add_bonus(80, 5, &adjusted) || adjusted != 85) return 1;
    if (add_bonus(INT_MAX, 1, &adjusted)) return 2;

    double floating = 0.1 + 0.2;
    if (fabs(floating - 0.3) >= 1e-9) return 3;

    int values[] = {80, 90, 75, 88, 92};
    int maximum;
    if (!max_array(values, 5, &maximum) || maximum != 92) return 4;
    if (max_array(values, 0, &maximum)) return 5;

    char line[8];
    if (snprintf(line, sizeof line, "%s", "Amy") < 0 || strcmp(line, "Amy") != 0) return 6;

    unsigned long long factorial;
    if (!factorial_checked(4, &factorial) || factorial != 24) return 7;
    if (factorial_checked(-1, &factorial)) return 8;

    int a = 10;
    int b = 20;
    if (!swap_values(&a, &b) || a != 20 || b != 10) return 9;
    if (!swap_values(&a, &a) || a != 20) return 10;

    Student student = {0};
    student.id = 1001;
    if (!set_name(&student, "Amy")) return 11;
    student.average = 90.0;
    if (strcmp(student.name, "Amy") != 0 || student.id != 1001 || student.average != 90.0) return 12;
    if (set_name(&student, "This name is much too long")) return 13;

    int *dynamic_values = malloc(3U * sizeof *dynamic_values);
    if (dynamic_values == NULL) return 14;
    for (int i = 0; i < 3; ++i) dynamic_values[i] = i * 10;
    if (dynamic_values[2] != 20) { free(dynamic_values); return 15; }
    free(dynamic_values);
    dynamic_values = NULL;

    FILE *file = tmpfile();
    if (file == NULL) return 16;
    if (fprintf(file, "%d\n", 80) < 0) { fclose(file); return 17; }
    rewind(file);
    int file_score;
    if (fscanf(file, "%d", &file_score) != 1 || file_score != 80) { fclose(file); return 18; }
    if (fclose(file) != 0) return 19;

    double average;
    if (!calculate_average(values, 5, &average) || fabs(average - 85.0) >= 1e-9) return 20;
    if (calculate_average(values, 0, &average)) return 21;

    if (!is_valid_score(0) || !is_valid_score(100) || is_valid_score(-1) || is_valid_score(101)) return 22;

    puts("all unit contracts passed");
    return 0;
}
