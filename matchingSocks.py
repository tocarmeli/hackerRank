def sockMerchant(n, ar):
	pairs = 0
	for i in ar:
		for j in ar[1:]:
			if j == i:
				pairs += 1
				ar.remove(j)
				ar.remove(i)
	print(pairs)



array = [1,2,1,2,1,3,2]

sockMerchant(7, array)