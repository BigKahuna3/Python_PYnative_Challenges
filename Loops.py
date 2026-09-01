# Exercise 1. Print first 10 natural numbers using while loop
count = 0
while count < 10:
    count += 1
    print(f"{count}")
    
# Exercise 2. Display numbers from -10 to -1 using for loop
for i in range(-10,0):
    print(i)
    
# Exercise 3. Display a message “Done” after successful execution of for loop
# Practice Problem: Write a program to display a message “Done” after the successful execution of a for loop that iterates from 0 to 4
for i in range(0,5):
    print(i)
print("Done!")

# Exercise 4. Calculate the sum of all numbers from 1 to N
# Practice Problem: Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.
def calculate_sum(end_number):
    return_number = 0
    if isinstance(end_number, int):
        last_number = end_number
    else:
        last_number = int(end_number)
    for i in range(1, last_number + 1):
        # print(f"{return_number} + {i} is:")
        return_number = return_number + i
        # print(f"{return_number}")
    return return_number

# force int (fails if text is given)
try:
    last_number = int(input("Enter last Number: "))
    print(f"The sum of all numbers from 1 to {last_number} is {calculate_sum(last_number)}")
except:
    print(f"ERROR: Input is not a number.  Rerun the program to try again... Continuing to the next method for now.")    

# allow text and convert int (does not fail if text is given, give me more control)
last_number = input("Enter last Number: ")
if last_number.isdigit():
    print(f"The sum of all numbers from 1 to {last_number} is {calculate_sum(last_number)}")
else:
    print(f"ERROR: {last_number} is not a number.  Rerun the program to try again... Continuing to the next Exersize for now.")

    