def isExactMultiple(input1,input2):
	if(input1==0 or input2==0):
		return 3;
	if(input1%input2==0):
		return 2
	return 1


input1 = int(input("Enter input1 : "))
input2 = int(input("Enter input2 : "))
res = isExactMultiple(input1,input2)
if(res==2):
	print("Exact multiple")
elif(res==1):
	print("Not exact multiple")
elif(res==0):
	print("input1 or input2 is zero")