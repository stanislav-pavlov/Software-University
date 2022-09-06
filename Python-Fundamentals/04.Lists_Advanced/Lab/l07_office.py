empl_happiness = list(map(int, input().split(" ")))
multiplicator = int(input())

happy_employees = list(filter(lambda x: x >= sum(empl_happiness) / len(empl_happiness), empl_happiness))

if len(happy_employees) >= len(empl_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(empl_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(empl_happiness)}. Employees are not happy!")