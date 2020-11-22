def digitSumEven(input1):
    Esum=0
    while(input1!=0):
        x = input1%10
        input1=input1//10
        if(x%2==0):
            Esum+=x
    return Esum

input1 = int(input("Enter the number : "))
res = digitSumEven(input1)
print("Even sum is : ",res)