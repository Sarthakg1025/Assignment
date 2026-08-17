class Arithmetic :
	def __init__(self):
		self.No1=0
		self.No2=0

	def Accept(self):
		self.No1=int(input("Enter The First Number : "))
		self.No2=int(input("Enter The Second Number : "))

	def Add(self):
		self.ret = self.No1 + self.No2
		return self.ret

	def Sub(self):
		self.ret2 = self.No1 - self.No2
		return self.ret2

	def Mul(self):
		self.ret3 = self.No1 * self.No2
		return self.ret3

	def Div(self):
		self.ret4 = self.No1 / self.No2
		#return self.ret4

	def Display(self):
		print("Addition is : ",self.ret)
		print("Subtraction is : ",self.ret2)
		print("Multiplication is : ",self.ret3)
		print("Division is : ",self.ret4)


obj=Arithmetic()
obj.Accept()
obj.Add()
obj.Sub()
obj.Mul()
obj.Div()
obj.Display()