def pw_check(pw):
    valid = True

    if len(pw) < 6 or len(pw) > 10:
        valid = False
        print("Password must be between 6 and 10 characters")
    if not pw.isalnum():
        valid = False
        print("Password must consist only of letters and digits")
    if sum(map(str.isdigit, pw)) < 2:
        valid = False
        print("Password must have at least 2 digits")

    if valid:
        print("Password is valid")


password = input()
pw_check(password)