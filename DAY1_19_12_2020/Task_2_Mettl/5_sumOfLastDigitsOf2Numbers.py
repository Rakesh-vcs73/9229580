def sumOfLastDigitsOf2Numbers(input1,input2):
    if(input1<0):
        input1=input1*(-1)
    if(input2<0):
        input2=input2*(-1)
    return (input1%10)+(input2%10)
    
input1=int(input("Enter input1 : "))
input2=int(input("Enter input2 : "))
res = sumOfLastDigitsOf2Numbers(input1,input2)
print("Sum of last 2 digts is : ",res)