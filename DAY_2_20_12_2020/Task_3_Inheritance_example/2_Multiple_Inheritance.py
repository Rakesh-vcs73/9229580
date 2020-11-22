class shirt:
	def __init__(self,color,size):
		self.Scolor=color
		self.Ssize=size
	def details(self):
		print("Shirt color : ",self.Scolor)
		print("Shirt size : ",self.Ssize)

class pant:
	def __init__(self,color,size):
		self.Pcolor=color
		self.Psize=size
	def details(self):
		print("Shirt color : ",self.Pcolor)
		print("Shirt size : ",self.Psize)

class suit(pant,shirt):
	def __init__(self,shirt_color,shirt_size,pant_color,pant_size,tie_color):
		self.tie_color=tie_color
		shirt.__init__(self,shirt_color,shirt_size)
		pant.__init__(self,pant_color,pant_size)
	def details(self):
		print("Suit Details : ")
		shirt.details(self)
		pant.details(self)
		print("Tie color : ",self.tie_color)


suit1 = suit("White",33,"Black",23,"Purple")
suit1.details() 
