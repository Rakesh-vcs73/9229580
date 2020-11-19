def N2ndlastDigitOfN(input1):
    if((input1<0 and input1>-10 )or(input1>0 and input1<10)or(input1==0)):
        return -1
    input1 = int(input1/10)
    if(input1<0):
        input1 = (-1)*input1
        return (-1)*(input1%10)
    return input1%10

input1 = int(input("Enter the number :"))
res = N2ndlastDigitOfN(input1)
print("2nd Last digit is: ",res)