def digitSumEvenOdd(input1,input2):
    Osum=0
    Esum=0
    while(input1!=0):
        x = input1%10
        input1=input1//10
        if(x%2==0):
            Esum+=x
        else:
            Osum+=x
    if(input2=="even"):
        return Esum
    if(input2=="odd"):
        return Osum

input1 = int(input("Enter the number : "))
input2 = input("Enter even or odd : ")
res = digitSumEvenOdd(input1,input2)
print("The ",input2," sum of ",input1," is --> ",res)