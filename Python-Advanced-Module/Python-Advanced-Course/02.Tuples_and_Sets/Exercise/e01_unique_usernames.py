count = int(input())
unique_usernames = set()

for _ in range(count):
    username = input()
    unique_usernames.add(username)

[print(x) for x in unique_usernames]