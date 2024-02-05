number=int(input("Enter the number: "))
if number>1:
    for i in range(2, number):
        if number%i==0:
            print("The number is not prime")
            break
    else:
        print("The number is prime") 