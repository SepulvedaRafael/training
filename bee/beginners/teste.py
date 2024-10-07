n = 6

num = 0
l = 1
m = 0

for j in range(n):
	num = m + l
	m = l
	l = num

	print(m)