#line = input().split()
#n, m = tuple(line)

n, m = tuple(map(int, input().split()))
n_set = set()
m_set = set()


for i in range(n):
    num = int(input())
    n_set.add(num)
for x in range(m):
    num = int(input())
    m_set.add(num)

[print(x) for x in n_set & m_set]