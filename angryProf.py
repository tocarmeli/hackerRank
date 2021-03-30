def angryProfessor(k, a):
	early = 0
	for time in a:
		if time <= 0:
			early += 1
	if early >= k:
		print("NO")
	else:
		print("YES")

ar = [-1,-1,0,0,1,1]

angryProfessor(4, ar)