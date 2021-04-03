def catAndMouse(x, y, z):
	if abs(z-x) < abs(z-y):
		print("Cat A")
	elif abs(z-x) > abs(z-y):
		print("Cat B")
	else:
		print("Mouse C")


catAndMouse(1,3,2)