def compareTriplets(a,b):
	alice_score = 0
	bob_score = 0
	for alice, bob in zip(a,b):
		if alice > bob:
			alice_score += 1
			bob_score += 0
		elif bob > alice:
			bob_score += 1
			alice_score += 0
		else:
			alice_score += 0
			bob_score += 0
			
	return alice_score, bob_score

al = [88, 22, 99]
bo = [82, 34, 98]

print (compareTriplets(al, bo))