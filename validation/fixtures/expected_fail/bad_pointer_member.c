typedef struct { int id; } Student;
int main(void) { Student value = {1}; Student *p = &value; return p.id; }
