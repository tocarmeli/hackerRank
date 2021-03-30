def diagonalDifference(arr):
	first_diagonal = arr[0] + arr[4] + arr[8]
	second_diagonal = arr[2] + arr[4] + arr[6]
	difference = abs(first_diagonal - second_diagonal)
	print(difference)


array = [11,2,4,4,5,6,10,8,-12]

diagonalDifference(array)