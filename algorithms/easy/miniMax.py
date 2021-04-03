def miniMax(arr):
	sorted_array = arr.sort()
	minimum = 0
	maximum = 0
	for small_nums in arr[0:-1]:
		minimum += small_nums

	for big_nums in arr[1:]:
		maximum += big_nums

	print(minimum)
	print(maximum)


ar = [1,5,3,7,9]

miniMax(ar)