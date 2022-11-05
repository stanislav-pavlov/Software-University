line = input().split(';')

for el in line:
    data = el.split('-')
    name = data[0]
    process_time = data[1]

    print(name)
    print(process_time)

starting_time = input().split(':')
hh = starting_time[0]
if len(hh) == 1:
    hh = int('0'+hh)
else:
    hh = int(starting_time[0])
mm = int(starting_time[1])
ss = int(starting_time[2])

print(hh)
print(mm)
print(ss)