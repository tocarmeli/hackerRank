# Will calculate whether Brian overcharged Anna when splitting a bill
# and if Brian buys something which Anna is allergic to

def bonAppetit(bill, k, b):
	bill.pop(k)
	totalAnna = 0
	for num in bill:
		totalAnna += num/2

	if totalAnna == b:
		print("Bon Appetit")

	else:
		print (int(b-totalAnna))
