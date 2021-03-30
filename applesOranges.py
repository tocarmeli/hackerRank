# Calculates how many oranges and apples will land on a house
# with start coordinates a and b
import random

def countApplesAndOranges(s, t, a, b, apples, oranges):
	apple_total = 0
	orange_total = 0
	for apple in apples:
		if apple + a >= s and apple + a <= t:
			apple_total += 1
		else:
			pass

	for orange in oranges:
		if orange + b >= s and orange + b <= t:
			orange_total += 1
		else:
			pass

	print (apple_total)
	print (orange_total)



ap_list = or_list = []

for i in range(5):
	num = random.randint(-10,10)
	ap_list.append(num)
	or_list.append(num)

countApplesAndOranges(5, 7, -1, 10, ap_list, or_list))