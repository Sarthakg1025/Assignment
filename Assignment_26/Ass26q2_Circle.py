class Circle:
	IP=3.14
	
	def __init__ (self):
		self.radius=0
		self.area=0
		self.circumference=0

	def Accept(self):
		self.r=int(input("Enter the radius of a Circle : "))

	def CalArea(self):
		self.ret1=Circle.IP * self.r * self.r
		
	def CalCircumference(self):
		self.ret2= 2 * Circle.IP * self.r 

	def Display(self):
		print("Area of Circle is : ",self.ret1)
		print("Circumference of Circle is :",self.ret2)
		
	

def main():
	obj=Circle()
	obj.Accept()
	obj.CalArea()
	obj.CalCircumference()
	obj.Display()

if __name__ == "__main__":
	main()