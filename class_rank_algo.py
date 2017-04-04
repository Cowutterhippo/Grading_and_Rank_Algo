class_A_grades = [99, 92, 91, 91, 89, 85, 83, 82, 80, 79, 78, 78, 77, 76, 75, 74, 62, 55, 43, 20]
class_B_grades = [56,36,66,88,90,99,100,43,76,76,76,76,44] 
class_C_grades = [66,78,65,90]
class_D_grades = [90,85,75,65,50] 
class_7_grades = [55,66,77,88,99,22,11] 


'''
Write a function that takes an arbitrary (possibly unsorted) score list of any
length (not necessarily the list used as an example above) as a parameter, and
returns a grade for each score.
'''

'''
A score in the top 20% of all scores is an A.
* A score in the next 20% of scores is a B.
* A score in the next 20% of scores is a C.
* A score in the next 20% of scores is a D.
* A score in the bottom 20% of scores is an F
'''


'''
As of now I am a mean teacher classes with sizes less than 4 cant get an A

'''




'''
psudo 
rank the list of grades [(99,1),(85,2),(84,3),(77,4), (66,5)]
apply code to all items rank/class_size * 100 = %tile
add the appropriate letter grade [(99,1,A),(85,2,B),(84,3,C),(77,4,D),(66,5,F)]

'''

'''
break up into more classes interface class, math class, class takes in the grades
write tests
make this a module
'''



class Grades:
	def __init__ (self, grades):
		self.grades = grades
		self.ranked_grades = self.apply_rank()
		self.class_size = self.check_class_size()
		self.letter_grades = self.apply_percentile_and_letter()


	def check_class_size(self):
		return len(self.grades)

	def apply_rank(self):
		sorted_grades = sorted(self.grades, reverse=True)
		return [grade for grade in enumerate(sorted_grades)]
		# reurns indexed grades
		# [(0, 99), (1, 88), (2, 77), (3, 66), (4, 55), (5, 22), (6, 11)]


	def apply_percentile_and_letter(self):
		for i in self.ranked_grades:
			percentile=((int(i[0])+1)/self.class_size) * 100
			if percentile <= 20:
				print ("grade:", i[1], "Rank:", i[0] + 1, "Percentile:", percentile, "Leter Grade: A")
			elif percentile >= 21 and percentile <= 40:
				print("grade:", i[1], "Rank:", i[0] + 1, "Percentile:", percentile, "Leter Grade: B")
			elif percentile >= 41 and percentile <= 60:
				print("grade:", i[1], "Rank:", i[0] + 1, "Percentile:", percentile, "Leter Grade: C")
			elif percentile >= 61 and percentile <= 80:
				print("grade:", i[1], "Rank:", i[0] + 1, "Percentile:", percentile, "Leter Grade: D")
			else:
				print("grade:", i[1], "Rank:", i[0] + 1, "Percentile:", percentile, "Leter Grade: F") 








		



if __name__ == "__main__":
	Grades(class_7_grades)
	Grades(class_A_grades)
	Grades(class_B_grades)
	Grades(class_C_grades)
	Grades(class_D_grades)


