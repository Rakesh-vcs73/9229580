def nFactorial(input1):
    fact=1
    while(input1!=1):
        fact*=input1
        input1-=1
    return fact
    
input1=int(input("Enter the input : "))
res=nFactorial(input1)
print("Factorial value is : ",res)