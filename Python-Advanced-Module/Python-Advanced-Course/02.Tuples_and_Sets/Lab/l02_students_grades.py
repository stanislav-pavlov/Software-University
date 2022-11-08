N = int(input())
students = {}

for _ in range(N):
    line = tuple(input().split())
    student, grade = line

    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for student, grades in students.items():
    grades_list_current_student = [str(f"{grade:.2f}") for grade in grades]
    average_grade = sum(grades) / len(grades_list_current_student)
    print(f"{student} -> {' '.join(grades_list_current_student)} (avg: {average_grade:.2f})")