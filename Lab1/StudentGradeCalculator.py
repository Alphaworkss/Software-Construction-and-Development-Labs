name = input("Enter your name: ")

math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
computer = float(input("Enter Computer marks: "))

average = (math + english + computer) / 3

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\nStudent Name:", name)
print("Average Marks:", average)
print("Grade:", grade)