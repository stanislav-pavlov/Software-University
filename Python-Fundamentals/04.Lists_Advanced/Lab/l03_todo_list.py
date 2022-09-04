todo_list = ["" for i in range(11)]
todo = input()

while todo != "End":
    todo_elements = todo.split("-")

    priority = int(todo_elements[0])
    task = todo_elements[1]
    todo_list[priority] = task

    todo = input()

sorted_list = [task for task in todo_list if task != ""]
print(sorted_list)
