# Will calculate how many times the highest points record has been broken and store it in index 0
# Least points record will be stored in index 1 of arrays

def breakingRecords(scores):
	high = low = scores[0]
	high_rec = low_rec = 0

	for score in scores:
		if score > high:
			high = score
			high_rec += 1
		elif score < low:
			low = score
			low_rec += 1

	return [high_rec, low_rec]