msg = input()
operation = input()


while operation != "Decode":
    operation_elements = operation.split("|")
    action = operation_elements[0]

    if action == "Move":
        letters_num = int(operation_elements[1])
        tracing_str = msg[:letters_num]
        static_str = msg[letters_num:]
        msg = static_str + tracing_str

    elif action == "Insert":
        index_num = int(operation_elements[1])
        new_char = operation_elements[2]
        first_part = msg[:index_num]
        second_part = new_char + msg[index_num:]
        msg = first_part + second_part

    elif action == "ChangeAll":
        sub_str = operation_elements[1]
        replacement_str = operation_elements[2]
        msg = msg.replace(sub_str, replacement_str)

    operation = input()

print(f"The decrypted message is: {msg}")