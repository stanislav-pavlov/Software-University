data = input()
courses = {}

# {key:{key:value}}
while ':' in data:
    info = data.split(':')
    name, id, course = info[0], int(info[1]), info[2]

    if course not in courses.keys():
        courses[course] = {}

# {basics/fundamentals: {5622: John}
    courses[course][id] = name

    data = input()

searched_course = data.replace('_', ' ')

for id in courses[searched_course]:
    print(f"{courses[searched_course][id]} - {id}")