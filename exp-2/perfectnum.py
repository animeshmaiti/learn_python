number=int(input("Enter the number: "))
def perfectNumber(number):
    temp=number//2
    # print(temp)
    sum=0
    for i in range(1, temp+1):
        if number%i==0:
            sum+=i
    if sum==number:
        print("The number is a perfect number")
    else:
        print("The number is not a perfect number")

perfectNumber(number)