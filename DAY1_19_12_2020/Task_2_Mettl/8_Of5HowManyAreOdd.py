def of5HowManyAreOdd(input1,input2,input3,input4,input5):
	count=0
	if(input1%2!=0 and input1!=0):
		count+=1
	if(input2%2!=0 and input2!=0):
		count+=1
	if(input3%2!=0 and input3!=0):
		count+=1
	if(input4%2!=0 and input4!=0):
		count+=1
	if(input5%2!=0 and input5!=0):
		count+=1
	return count


input1 = int(input("Enter input1 : "))
input2 = int(input("Enter input2 : "))
input3 = int(input("Enter input3 : "))
input4 = int(input("Enter input4 : "))
input5 = int(input("Enter input5 : "))
res = of5HowManyAreOdd(input1,input2,input3,input4,input5)
print("Count of odd numbers are : ",res)