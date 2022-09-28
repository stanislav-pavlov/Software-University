courses_dict = {}
line = input()

while line != "end":
    data = line.split(' : ')
    course = data[0]
    student = data[1]

    if course not in courses_dict.keys():
        courses_dict[course] = [student]
    else:
        courses_dict.setdefault(course, [])
        courses_dict[course].append(student)

    line = input()

for k in courses_dict.keys():
    print(f"{k}: {len(courses_dict[k])}")
    for student in courses_dict[k]:
        print(f"-- {student}")