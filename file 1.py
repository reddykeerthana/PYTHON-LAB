# Student Information and Academic Summary

# Accept student details
name = input("Enter Student Name: ")
usn = input("Enter USN: ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")

# Accept three subject marks
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# Calculate total and average
total = mark1 + mark2 + mark3
average = total / 3

# Display formatted output
print("\n" + "=" * 40)
print("       STUDENT ACADEMIC SUMMARY")
print("=" * 40)

print(f"Student Name : {name}")
print(f"USN          : {usn}")
print(f"Branch       : {branch}")
print(f"Semester     : {semester}")

print("-" * 40)
print(f"Subject 1 Marks : {mark1}")
print(f"Subject 2 Marks : {mark2}")
print(f"Subject 3 Marks : {mark3}")
print("-" * 40)

print(f"Total Marks   : {total:.2f}")
print(f"Average Marks : {average:.2f}")

print("=" * 40)
