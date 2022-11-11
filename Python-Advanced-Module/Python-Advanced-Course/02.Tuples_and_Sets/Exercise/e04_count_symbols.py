line = input()
symbols_dict = dict()

for sym in line:
    if sym not in symbols_dict:
        symbols_dict[sym] = 1
    else:
        symbols_dict[sym] += 1

for key, value in sorted(symbols_dict.items()):
    print(f"{key}: {value} time/s")