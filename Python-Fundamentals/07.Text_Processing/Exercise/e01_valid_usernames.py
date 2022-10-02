all_usernames_list = input().split(', ')
valid_usernames_list = []

for username in all_usernames_list:
    if 3 < len(username) < 16:
        if username.isalnum() or '_' in username or '-' in username:
            valid_usernames_list.append(username)

[print(f"{username}") for username in valid_usernames_list]