def isOdd(input1):
	if(input1%2!=0):
		return 1
	else:
		return 2

input1=int(input("Enter a number : "))
res = isOdd(input1)
if(res==1):
	print("ODD")
if(res==2):
	print("EVEN")