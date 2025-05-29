score = int(input("Enter your score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
print("Your grade is:", grade)

# This program takes the student’s score as input. It then uses a chain of if statements to check for specific score ranges and assigns the corresponding letter grade