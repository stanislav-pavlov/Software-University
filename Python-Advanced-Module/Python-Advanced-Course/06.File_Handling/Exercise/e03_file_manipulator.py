import os

command = input()
while command != "End":
    command = command.split('-')
    action = command[0]
    file_name = command[1]

    if action == "Create":
        file = open(f"{file_name}", 'w')
        file.close()
    elif action == "Add":
        content = command[2]
        with open(f"{file_name}", 'a') as file:
            file.write(content + '\n')
    elif action == "Replace":
        old_str = command[2]
        new_str = command[3]
        try:
            with open(f"{file_name}", 'r') as file:
                text = file.readlines()

            file = open(f"{file_name}", 'w')
            # for row in text:
            #     row = row.replace(old_str, new_str)     ---> does not work, why?

            for i in range(len(text)):
                text[i] = text[i].replace(old_str, new_str)
            file.write(''.join(text))
            file.close()
        except FileNotFoundError:
            print("An error occurred")
    elif action == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
    else:
        break
    command = input()