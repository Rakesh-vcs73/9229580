class cat:
	species = 'mammal'
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def get_age(self):
		return self.age

cat1 = cat("Tom",5)
cat2 = cat("Oggy",6)
cat3 = cat("catty",2)
def maxAge(cat1,cat2,cat3):
	x = max(cat1.get_age(),cat2.get_age(),cat3.get_age())
	print("The oldest cat is ",x," years old")
maxAge(cat1,cat2,cat3)
