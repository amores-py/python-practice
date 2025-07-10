#Problem Statement:  Write a Python program that:
#1. 	Takes an integer input from the user.
#2. 	Checks whether the number is even or odd using an if-else statement.
#3. 	Displays the result accordingly.
'{Task 1}'
number=int(input("pleace enter the number: "))
if number % 2==0:
    print(f"{number} is a even number")
else:
    print(f"{number} is a odd number")

'''Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
'''
'Task 2'
total= 0
for number in range(1, 51):  
    total += number
print(f"the sum of numbers from 1 to 50 is :{total}")
