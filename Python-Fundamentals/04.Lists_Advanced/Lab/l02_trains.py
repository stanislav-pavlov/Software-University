wagons_count = int(input())
wagons_list = [0 for num in range(wagons_count)]
command = input()

while command != "End":
    cmd_elements = command.split(" ")
    current_command = cmd_elements[0]
    if current_command == "add":
        people = int(cmd_elements[1])
        wagons_list[-1] += people

    if current_command == "insert":
        nr_of_wagon = int(cmd_elements[1])
        people = int(cmd_elements[2])
        wagons_list[nr_of_wagon] += people

    if current_command == "leave":
        nr_of_wagon = int(cmd_elements[1])
        people = int(cmd_elements[2])
        wagons_list[nr_of_wagon] -= people

    command = input()

print(wagons_list)