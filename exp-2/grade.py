marks=(int(x) for x in input("Enter the marks: ").split())
total=0
full_marks=500
for mark in marks:
    total+=mark
percentage=total/full_marks*100
if percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("Grade B")
elif percentage>=70:
    print("Grade C")
elif percentage>=60:
    print("Grade D")
else:
    print("Grade F")