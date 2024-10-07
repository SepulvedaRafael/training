n, p, d = int(input()), map(int, input().split()), {}

for i, v in enumerate(p):
    d[v] = i + 1
for i in range(n):
    print(d[i+1])