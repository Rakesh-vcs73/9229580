def digitSumOdd(input1):
    Osum=0
    while(input1!=0):
        x = input1%10
        input1=input1//10
        if(x%2!=0):
            Osum+=x
    return Osum

input1 = int(input("Enter the number : "))
res = digitSumOdd(input1)
print("Odd sum is : ",res)