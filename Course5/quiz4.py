# Initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# Seek user input for ten numbers 
for i in range(10):
    userInput = input("Enter any 2-digit number: ")
    
# Check to see if number is even and if yes, add to list_sum
# Print incorrect value warning when ValueError exception occurs
    try:
        number = int(userInput)
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Incorrect value. That's not an int!")

print(f"user_list: {user_list}")
print(f"The sum of the even numbers in user_list is: {list_sum}.")