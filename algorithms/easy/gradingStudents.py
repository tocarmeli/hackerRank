rand_grades = [3, 21, 29, 97]

"""
def gradingStudents(grades):
	for grade in grades:
		if grade < 40:
			return grade

		rounded_num = 5 * round(grade/5)

		if grade > 38:
			return rounded_num

print(gradingStudents(rand_grades))
"""

def gradingStudents(grades):
	grades.pop(0)
	
	for i in grades:
		if i < 38:
			print (i)

		else:

			rounded_num = 5 * round(i/5)
			if i%5 == 1 or i%5 == 2:
				rounded_num += 5
			if rounded_num - i >= 3:
				print (i)
			else:
				print(rounded_num)


gradingStudents(rand_grades)