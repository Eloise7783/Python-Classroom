from abc import ABC
class Polygon(ABC):
	def __init__(self, numberOfSides):
		self.numberOfSides = numberOfSides

class Triangle(Polygon):
	def triPerimeter(self, side1L, side2L, side3L):
		outerEdge = side1L + side2L + side3L
		return(outerEdge)
	def triAarea(self, base, height):
		theInside = base * height / 2
		return(theInside)

class Quadrilateral(Polygon):
	def quadPerimeter(self, side1L, side2L, side3L, side4L):
		outerEdge = side1L + side2L + side3L + side4L
		return(outerEdge)
	def quadArea(self, length, width):
		theInside = length * width
		return(theInside)

bob = Triangle(3)
bobsPerim = bob.triPerimeter(15,30,19)
print(bobsPerim,"cm")
bobsArea = bob.triArea(30,19)
print(bobsArea,"cm2")

quin = Quadrilateral(4)
quinsPerim = quin.quadPerimeter(15,85,99,10)
print(quinsPerim, "cm")
quinsArea = quin.quadArea(15,99)
print(quinsArea,"cm2")