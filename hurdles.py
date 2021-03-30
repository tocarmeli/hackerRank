def hurdleRace(k, height):
	elevation = k + 1
	potionCount = 0
	for h in height:
		if k < h:
			potionCount += 1

	print(potionCount)


heights = [1,6,3,5,2]

hurdleRace(4, heights)