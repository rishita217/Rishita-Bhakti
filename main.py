# Python Program to Calculate Age to 100

# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Calculating the year they will turn 100
current_year = 2025
year_when_100 = current_year + (100 - age)

# Output
print(f"Hello {name}! You will turn 100 years old in the year {year_when_100}.")