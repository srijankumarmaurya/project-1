print("Welcome to the Interactive Student Data Collector!")
print()
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favourite_number = int(input("Please enter your favourite number: "))
print()
print()
current_year = 2026
birth_year = current_year - age

print("Thank you! Here is the information we collected:")
print()
# Display Information
print(f"\nYour Name is : {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"\nYour age is : {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"\nYour height is : {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"\nYour favourite number is: {favourite_number} (Type: {type(favourite_number)}, Memory Address: {id(favourite_number)})")
print()
print(f"\nYour birth year is approximately: {birth_year} (based on your age of {age})")
print()
print("\nThank you for using the Student Data Collector. Goodbye!")
