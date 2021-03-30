# Will find if 2 consecutive ints in a list if they are added together
# can be divided by num k evenly

def divisbleSumPairs(n, k, ar):
	total = 0
	for i in range(n):
		for j in range(i+1, n):
			if (ar[i] + ar[j]) % k == 0:
				total += 1
			else:
				pass
	return total

array = [1,2,3,4,5,6]

print(divisbleSumPairs(6, 5, array))