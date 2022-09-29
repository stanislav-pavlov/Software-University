line = input()
results_dict = {}
banned_users = []
full_languages_dict = {}

while line != "exam finished":
    data = line.split('-')

    if "banned" in data:
        banned_users.append(data[0])
    else:
        username, language, points = data[0], data[1], int(data[2])

        if language not in full_languages_dict.keys():
            full_languages_dict[language] = 1
        else:
            full_languages_dict[language] += 1

        if username not in results_dict.keys():
            results_dict[username] = {}

        if language not in results_dict[username]:
            results_dict[username][language] = points
        elif points > results_dict[username][language]:
            results_dict[username][language] = points

    line = input()

print("Results:")
for user in results_dict.keys():
    [print(f"{user} | {results_dict[user][lan]}") for lan in results_dict[user] if user not in banned_users]

print("Submissions:")
for k, v in full_languages_dict.items():
    print(f"{k} - {v}")