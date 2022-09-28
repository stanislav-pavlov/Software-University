n = int(input())
students_dict = {}


for i in range(n):
    student_name = input()
    grade = float(input())
    grade_count = 1

    if student_name not in students_dict.keys():
        students_dict[student_name] = grade / grade_count
    else:
        grade_count += 1
        students_dict[student_name] = (students_dict[student_name] + grade) / grade_count

for key, value in students_dict.items():
    if value >= 4.5:
        print(f"{key} -> {value:.2f}")