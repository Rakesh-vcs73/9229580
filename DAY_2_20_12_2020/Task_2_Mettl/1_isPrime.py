def isPrime(input1):
	flag=0
	for i in range(2,(input1//2)+2):
		if(input1%i==0):
			flag=1
	if flag==1:
		return 1
	else:
		return 2

input1=int(input("Enter the number : "))
res=isPrime(input1)
if res==1:
	print("NOT PRIME")
else:
	print("PRIME")
