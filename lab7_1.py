from math import pi

#class for sphere
class Sphere(object) :
	#constructor of class
	def __init__(self, radius = 1, x = 0 , y = 0, z = 0) :	#initial values of variables if user did not define them
		#variables of this instance are equal to arguments
		self.radius = radius
		self.x = x
		self.y = y
		self.z = z


	#function which calculates and returns the volume of sphere
	def get_volume(self) :
		volume = 4.0 / 3.0 * pi * pow(self.radius, 3)
		return volume


	#function which calculates and returns the square of sphere
	def get_square(self) :
		square = 4 * pi * pow(self.radius, 2)
		return square

	
	#function which returns radius of sphere
	def get_radius(self) :
		return self.radius

	
	#function which returns the tuple with center coordinates
	def get_center(self) :
		return (self.x, self.y, self.z)

	
	#function that sets the radius of the sphere with argument
	def set_radius(self, r) :
		self.radius = r


	#function that sets the center of the sphere with 3 arguments
	def set_center(self, x, y, z) :
		self.x = x
		self.y = y
		self.z = z


	#function that returns True if point with coordinates from arguments is inside the sphere and False in else-case
	def is_point_inside (self, x, y, z) :
		if pow(x - self.x, 2) + pow(y - self.y, 2) + pow(z - self.z, 2) < pow(self.radius, 2) :
			return True
		else :
			return False
