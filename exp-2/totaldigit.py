number=(int(input("Enter the number: ")))
count=0
while number>0:
    number=number//10
    count+=1
print("The total number of digits in the number is", count)