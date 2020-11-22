def NoOfPrimeInaRange(input1,input2):
    count=0
    if(input1==1):
        input1+=1
    for i in range(input1,input2+1):
        flag=0
        for j in range(2,(i//2)+1):
            if(i%j==0):
                flag=1
                break
        if(flag==0):
            #print(i)
            count+=1
    return count

input1=int(input("Enter first number : "))
input2=int(input("Enter second number : "))
res=NoOfPrimeInaRange(input1,input2)
print("Count : ",res)