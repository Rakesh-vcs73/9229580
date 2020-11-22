def AllDigitsCount(input1):
    inp=str(input1)
    return len(inp)
    
input1 = int(input("Enter the number : "))
res = AllDigitsCount(input1)
print("Digit count of {} is : {}".format(input1,res))