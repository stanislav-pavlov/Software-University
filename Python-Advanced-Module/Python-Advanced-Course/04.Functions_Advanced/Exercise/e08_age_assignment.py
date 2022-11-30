def age_assignment(*args, **kwargs):
    result = ''

    for name in sorted(args):
        age = 0
        for key, value in kwargs.items():
            if name[0] == key:
                age += value
        result += f"{name} is {age} years old." + '\n'

    return result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))