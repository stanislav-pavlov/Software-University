def reverse_text(text):
    idx = -1

    while idx >= -len(text):
        yield text[idx]
        idx -= 1



for char in reverse_text("step"):
    print(char, end='')


#          s  t  e  p     len = 4
#         -4 -3 -2 -1
#          0  1  2  3