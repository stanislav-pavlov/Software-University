line = input()
employees_dict = {}

while line != "End":
    data = line.split(" -> ")
    company = data[0]
    employee_id = data[1]

    if company not in employees_dict.keys():
        employees_dict[company] = [employee_id]
    else:
        employees_dict.setdefault(company, [])
        if employee_id not in employees_dict[company]:
            employees_dict[company].append(employee_id)

    line = input()

for k in employees_dict.keys():
    print(f"{k}")
    for employee in employees_dict[k]:
        print(f"-- {employee}")