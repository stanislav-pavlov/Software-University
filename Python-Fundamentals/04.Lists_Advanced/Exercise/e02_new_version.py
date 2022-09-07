def new_version(old_ver):
    new_ver_num = int("".join(initial_version)) + 1
    final_ver = ".".join(str(new_ver_num))
    print(final_ver)


initial_version = input().split(".")
new_version(initial_version)