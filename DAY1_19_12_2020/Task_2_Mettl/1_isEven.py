def isEven(input1):
	if(input1%2==0):
		return 2
	else:
		return 1

input1=int(input("Enter a number : "))
res = isEven(input1)
if(res==2):
	print("EVEN")
if(res==1):
	print("ODD")