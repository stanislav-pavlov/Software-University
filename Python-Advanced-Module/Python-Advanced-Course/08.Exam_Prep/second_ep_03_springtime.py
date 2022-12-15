def start_spring(**kwargs):
    reversed_dict = {}
    for key, value in kwargs.items():
        if value not in reversed_dict:
            reversed_dict[value] = []
        reversed_dict[value].append(key)

    result = ''
    for key, value in sorted(reversed_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{key}:\n"
        for item in sorted(value):
            result += f"-{item}\n"

    return result


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
