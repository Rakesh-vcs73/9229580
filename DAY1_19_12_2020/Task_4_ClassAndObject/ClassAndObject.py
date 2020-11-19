"""
1)Create laptop object with cost and processor speed as attributes
2)find laptop with less cost and laptop with more processor speed
3)print the selected laptops
"""

class laptop:
	def __init__(self,cost,speed):
		self.cost=cost
		self.processor_speed=speed

hp = laptop(45000,2.2)
dell = laptop(50000,3.0)
apple  = laptop(100000,2.3)
def minCost(hp,dell,apple):
	minC=min(hp.cost,dell.cost,apple.cost)
	return minC
def maxSpeed(hp,dell,apple):
	maxP = max(hp.processor_speed,dell.processor_speed,apple.processor_speed)
	return maxP
print("Laptop with less cost is : INR ",minCost(hp,dell,apple))
print("Laptop with high processor speed is : ",maxSpeed(hp,dell,apple)," GHz")