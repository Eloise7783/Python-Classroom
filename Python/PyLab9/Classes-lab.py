class Student:
	def __init__(self, namevar, agevar, classvar):
		self.name = namevar
		self.age = agevar
		self.subject = classvar

	def marks(self, mark1, mark2, mark3):
		avgMarks = mark1 + mark2 + mark3 / 3
		return avgMarks

student1 = Student("Eloise","22","DevOps")
student2 = Student("John","19","Music")

student1Marks = Student.marks(student1,90,15,80)
print("Your average marks are", student1Marks)