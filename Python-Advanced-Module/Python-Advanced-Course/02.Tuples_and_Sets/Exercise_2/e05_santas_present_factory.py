from collections import deque

materials_stk = list(map(int, input().split()))
magic_q = deque(map(int, input().split()))
presents_dict = {
    "Doll": {
        "magic_level": 150,
        "crafted": 0
    },
    "Wooden train": {
        "magic_level": 250,
        "crafted": 0
    },
    "Teddy bear": {
        "magic_level": 300,
        "crafted": 0
    },
    "Bicycle": {
        "magic_level": 400,
        "crafted": 0
    }
}
reverse_stack = []

while materials_stk and magic_q:
    flag = False
    if materials_stk[-1] == 0:
        materials_stk.pop()
        flag = True
    if magic_q[0] == 0:
        magic_q.popleft()
        flag = True
    if flag:
        continue

    material = materials_stk.pop()
    magic = magic_q.popleft()
    product = material * magic
    if product == presents_dict["Doll"]["magic_level"]:
        presents_dict["Doll"]["crafted"] += 1
    elif product == presents_dict["Wooden train"]["magic_level"]:
        presents_dict["Wooden train"]["crafted"] += 1
    elif product == presents_dict["Teddy bear"]["magic_level"]:
        presents_dict["Teddy bear"]["crafted"] += 1
    elif product == presents_dict["Bicycle"]["magic_level"]:
        presents_dict["Bicycle"]["crafted"] += 1
    elif product < 0:
        new_material = material + magic
        materials_stk.append(new_material)
    elif product > 0:
        new_material = material + 15
        materials_stk.append(new_material)

if presents_dict["Doll"]["crafted"] > 0 and presents_dict["Wooden train"]["crafted"] > 0 or presents_dict["Teddy bear"]["crafted"] > 0 and presents_dict["Bicycle"]["crafted"] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_stk:
    for _ in range(len(materials_stk)):
        reverse_stack.append(materials_stk.pop())
    print(f"Materials left: {', '.join(map(str, reverse_stack))}")
if magic_q:
    print(f"Magic left: {', '.join(map(str, magic_q))}")

for present in sorted(presents_dict):
    if presents_dict[present]["crafted"] > 0:
        print(f"{present}: {presents_dict[present]['crafted']}")