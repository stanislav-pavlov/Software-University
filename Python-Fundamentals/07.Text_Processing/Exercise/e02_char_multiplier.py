line = input().split()
ascii_nums1 = []
ascii_nums2 = []

res = 0

for ch in line[0]:
    ascii_nums1.append(ord(ch))
for ch in line[1]:
    ascii_nums2.append(ord(ch))

for num1, num2 in zip(ascii_nums1, ascii_nums2):
    res += num1 * num2

if len(ascii_nums2) > len(ascii_nums1):
    diff = int(len(ascii_nums2) - len(ascii_nums1))
    for i in ascii_nums2[:-diff-1:-1]:
        res += i
else:
    diff = int(len(ascii_nums1) - len(ascii_nums2))
    for i in ascii_nums1[:-diff-1:-1]:
        res += i

print(res)