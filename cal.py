print("-----SIMPLE CALCULATOR-----")

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

print("SELECT YOUR CHOICE: ")
print('1.ADD\n 2.SUBTRACT\n 3.MULTIPLY\n 4.DIVIDE')

choice = int(input("ENTER YOUR CHOICE (1/2/3/4): "))

if choice == 1:
    result = num_1 + num_2
    print(f"The sum of two numbers is: {result}")
elif choice == 2:
    result = num_1 - num_2
    print(f"The difference between two numbers is: {result}")
elif choice == 3:
    result = num_1 * num_2
    print(f"The product of two numbers is: {result}")
elif choice == 4:
    result = num_1 / num_2
    print(f"The quotient of two numbers is: {result}")
else:
    print("Invalid choice! Please try again. Thank you!")
