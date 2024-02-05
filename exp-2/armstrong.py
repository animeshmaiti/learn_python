number=int(input("Enter the number: "))

def countDigit(number):
    count=0
    while number>0:
        number=number//10
        count+=1
    return count

def armStrongNumber(number):
    count=countDigit(number)
    temp=number
    sum=0
    while temp>0:
        digit=temp%10
        sum+=(digit**count)
        temp=temp//10
    if sum==number:
        print("The number is a armstrong number")
    else:
        print("The number is not a armstrong number")

armStrongNumber(number)