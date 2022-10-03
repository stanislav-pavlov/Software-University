def extract_file(address):
    last_element = address[-1].split('.')
    name = last_element[0]
    extension = last_element[1]
    print(f"File name: {name}")
    print(f"File extension: {extension}")


line = input().split("\\")
extract_file(line)
