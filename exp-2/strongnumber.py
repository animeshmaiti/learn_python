number=int(input("Enter the number: "))
def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)
    
def strongNumber(number):
    temp=number
    sum=0
    while temp>0:
        digit=temp%10
        sum+=factorial(digit)
        temp=temp//10
    if sum==number:
        print("The number is a strong number")
    else:
        print("The number is not a strong number")

strongNumber(number)