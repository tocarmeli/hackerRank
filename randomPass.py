import random
import string

num_pass = int(input("How many characters do you want your password to be? "))

lower_upper_alphabet = string.ascii_letters

def rand_pass():
	for i in range(num_pass):
		rand_num = random.randint(1,2) # chooses a num between 1 and 2. If num is 1, it will print a number. If num is 2, it will print letter
		if rand_num == 1:
			rand_pass_num = int(random.randint(0,9))  # Chooses random num for password
			print(rand_pass_num)
		elif rand_num:
			rand_pass_letter = random.choice(lower_upper_alphabet)
			print(rand_pass_letter)

rand_pass()