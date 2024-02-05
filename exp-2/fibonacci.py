number=int(input("Enter the number: "))

def numIsPresentInFibonacciSeries(number):
    a=0
    b=1
    while a<=number:
        if a==number:
            print("The number is present in the fibonacci series")
            break
        else:
            c=a+b
            a=b
            b=c
    else:
        print("The number is not present in the fibonacci series")