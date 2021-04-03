def utopianTree(n):
	height = 1
	i = 0
	while i < n:
		if i % 2 == 0:
			height = height * 2
		else:
			height += 1
			i += 1

print(height)

utopianTree(5)