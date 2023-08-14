from abc import ABC, abstractmethod
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

class Bird(ABC):
	def __init__(self, wingspan, size, flies):
		self.wingspan = wingspan
		self.size = size
		self.flies = flies

	abstractmethod
	def nocturnal(self):
		pass
	abstractmethod
	def extinct(self):
		pass

class Owl(Bird):
	def nocturnal():
		True

class Dodo(Bird):
	def extinct():
		True

John = Owl("5m","1m",True)
John.nocturnal = True

print(John.wingspan)

Dodie = Dodo("1m","2m",False)
Dodie.extinct = True



