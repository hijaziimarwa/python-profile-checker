name = input("Enter your name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your score (0-5): "))
field_of_interest = input("Enter your field of interest: ")
has_graduated = input("Are you graduated? (yes/no): ")

print("========= Student Profile ==========")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"GPA: {gpa}")
print(f"Field of interest: {field_of_interest}")
print(f"Graduated: {has_graduated}")
print("====================================")

if age<25 and gpa>=3.5 and has_graduated=="yes":
    print("Congrats! You are eligible for a scholarship")
elif age<30 and gpa>=2.5:
    print("You are eligible for an internship")
else:
    print("Sorry! Apply again later")
