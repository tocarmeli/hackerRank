# Will calculate the number of valleys a hiker traversed through
# A valley is when the hiker makes to or steps down


def countingValleys(n, s):
	seaLevel = valley = 0

	for step in s:
		if step == "U":
			seaLevel += 1

		else:
			seaLevel -= 1

		if step == "U" and seaLevel == 0:
			valley += 1

	return valley