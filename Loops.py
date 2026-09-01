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
    last_number = int(input("Exercise 4 - Enter last Number: "))
    print(f"The sum of all numbers from 1 to {last_number} is {calculate_sum(last_number)}")
except:
    print(f"ERROR: Input is not a number.  Rerun the program to try again... Continuing to the next method for now.")    

# allow text and convert int (does not fail if text is given, give me more control)
last_number = input("Exercise 4.2 - Enter last Number: ")
if last_number.isdigit():
    print(f"The sum of all numbers from 1 to {last_number} is {calculate_sum(last_number)}")
else:
    print(f"ERROR: {last_number} is not a number.  Rerun the program to try again... Continuing to the next Exersize for now.")


'''
Exercise 4. (really 5) Print multiplication table of a given number
Practice Problem: Create a program that takes an integer and prints its multiplication table from 1 to 10.
'''
def calculate_multiplication_table(multiplier: int):
    if multiplier > 0:
        for i in range(1, 11):
            print(f"{i * multiplier}")


# allow text and convert int (does not fail if text is given, give me more control)
multiple_number = input("Exercise 5 - Enter multiple Number: ")
if multiple_number.isdigit():
    calculate_multiplication_table(int(multiple_number))
else:
    print(f"ERROR: {multiple_number} is not a number.  Rerun the program to try again... Continuing to the next Exersize for now.")


'''
Exercise 6. Calculate the cube of all numbers from 1 to a given number
Practice Problem: Write a program that takes an integer n and prints the cube of every number from 1 to n in the format Current Number is : 1 and the cube is 1.
'''
number = input("Exercise 6 - Enter number of numbers to cube: ")
if number.isdigit():
    for i in range(1, int(number) + 1):
        print(f"Current Number is : {i} and the cube is {i ** 3}")
else:
    print(f"ERROR: {number} is not a number.  Rerun the program to try again... Continuing to the next Exersize for now.")


'''
Exercise 7. Display numbers from a list using a loop
Practice Problem: Given a list of numbers, iterate through it and print numbers that satisfy these conditions:
    The number must be divisible by five.
    If the number is greater than 150, skip it and move to the next.
    If the number is greater than 500, stop the loop entirely.
'''
numbers = [12, 75, 150, 180, 145, 525, 50]
print("Exercise 7")
for i in numbers:
    # condition 1 - multiple of 5
    if i % 5 == 0:
        # condition 2 - skip if > 150
        if i <= 150:
            print(i)
        else:
            # condition 3 stop if > 500
            if i > 500:
                break
            
# another way
print("Exercise 7 (alternate)")
for i in numbers:
    # condition 3 - stop if > 500
    if i > 500:
        break
    # condition 2 - if > 150 skip
    if i > 150:
        continue
    # condition 1 - print if multiple of 5
    if i % 5 == 0:
        print(i)


'''
Exercise 8. Count occurrences of a specific element in a list
Practice Problem: Given a list of numbers, use a loop to count 
how many times a specific number (e.g., 10) appears.

Exercise Purpose: This introduces Frequency Counting, a staple 
of data analysis. It shows how to iterate through a collection 
and use a conditional filter to increment a tally only when a match is found.
'''
list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10
count = 0
for i in list1:
    if i == target:
        count += 1
        
print(f"Exercise 8: {target} appears {count} times")

'''
Exercise 9. Print elements from a list present at odd index positions
Practice Problem: Given a Python list, use a loop to print only the elements 
that are located at odd index positions (index 1, 3, 5, etc.).

Exercise Purpose: This exercise teaches Index-Based Iteration. It helps you 
distinguish between an item’s value in a list and its position (index), which 
is fundamental for data filtering.

Given Input: my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

Expected Output: [20 40 60 80 100]
'''
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
result_list = []
for i in range(0, len(my_list)):
    if i % 2:
        result_list.append(my_list[i])
        
print(f"Exercise 9: {result_list}")

'''
Exercise 10. Print list in reverse order using a loop
Practice Problem: Given a list, iterate it in reverse order and print each element.

Exercise Purpose: Learning to Traverse Data Backwards is essential for many data structures. 
This exercise shows how to use the reversed() function or custom range slicing to iterate 
over a list from the end to the beginning.

Given Input: list1 = [10, 20, 30, 40, 50]
Expected Output: [50, 40, 30, 20, 10]
'''
list1 = [10, 20, 30, 40, 50]
result_list = []
for i in range(len(list1), 0, -1):
    result_list.append(list1[i - 1])
print(f"Exercise 10: {result_list}")

result_list = []
for i in reversed(list1):
    result_list.append(i)
print(f"Exercise 10 using reversed: {result_list}")

list1.reverse() # this changes list1
print(f"Exercise 10 using reverse: {list1}")


