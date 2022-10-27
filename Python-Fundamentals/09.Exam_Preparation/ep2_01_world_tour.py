stops = input()
command = input()

while command != "Travel":
    command = command.split(":")
    action = command[0]

    if action == "Add Stop":
        insert_index = int(command[1])
        insert_stop = command[2]
        if 0 <= insert_index <= len(stops):
            stops = stops[:insert_index] + insert_stop + stops[insert_index:]
    elif action == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index+1:]

    elif action == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)

    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")

