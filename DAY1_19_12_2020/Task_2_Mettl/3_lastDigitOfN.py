def lastDigitOfN(input1):
	if(input1<0):
		input1 = input1*(-1)
		return (-1)*(input1%10)
	return input1%10

input1 = int(input("Enter the number :"))
res = lastDigitOfN(input1)
print("Last digit is: ",res)