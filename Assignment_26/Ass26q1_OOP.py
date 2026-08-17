class Demo:
	value=0

	def __init__ (self,No1,No2):
		self.No1=No1
		self.No2=No2

	def Fun(self):
		print(self.No1)
		print(self.No2)

	def Gun(self):
		print(self.No1)
		print(self.No2)

dobj1=Demo(11,21)
dobj2=Demo(51,101)

dobj1.Fun()
dobj2.Fun()
dobj1.Gun()
dobj2.Gun()	