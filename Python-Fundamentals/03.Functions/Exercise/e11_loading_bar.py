def loading_bar(num):
    percentage_syms = "%" * int(num / 10)
    dot_syms = "." * int(10 - num / 10)

    if num == 100:
        print(f"{num}% Complete!")
        print(f"[{percentage_syms}]")
    elif 0 <= (num % 10 == 0) <= 90:
        print(f"{num}% [{percentage_syms}{dot_syms}]")
        print("Still loading...")


percentage_num = int(input())
loading_bar(percentage_num)