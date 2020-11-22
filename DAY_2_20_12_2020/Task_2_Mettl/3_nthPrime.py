def nthPrime(input1):
    if input1==1:
        return 2
    count=1
    i=3
    while(count!=input1):
        flag=0
        for j in range(2,(i//2)+1):
            if(i%j==0):
                flag=1
        if(flag==0):
            count+=1
            #print(i)
        i+=1
    return i-1

input1=int(input("Enter the number : "))
res=nthPrime(input1)
print(input1,"th prime number is : ",res)