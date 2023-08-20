# # PYTHON PROGRAMMING LANGUGE ASSIGNMENT

# # QUESTION NO #1
# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Cannot divide by zero!"
#     return x / y

# def power(x, y):
#     return x ** y

# print("Select operation:")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
# print("5. Power")

# choice = input("Enter choice (1/2/3/4/5): ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if choice == '1':
#     print(num1, "+", num2, "=", add(num1, num2))
# elif choice == '2':
#     print(num1, "-", num2, "=", subtract(num1, num2))
# elif choice == '3':
#     print(num1, "*", num2, "=", multiply(num1, num2))
# elif choice == '4':
#     print(num1, "/", num2, "=", divide(num1, num2))
# elif choice == '5':
#     print(num1, "^", num2, "=", power(num1, num2))
# else:
#     print("Invalid input")

# QUESTION NO # 2
# def has_numeric_value(lst):
#     for item in lst:
#         if isinstance(item, (int, float)):
#             return True
#     return False

# # Example list
# my_list = [1, 'apple', 3.14, 'banana', '5']

# if has_numeric_value(my_list):
#     print("The list contains numeric values.")
# else:
#     print("The list does not contain any numeric values.")

# # QUSTION NO # 3
# # Initial dictionary
# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# # Adding a new key-value pair
# my_dict['occupation'] = 'Engineer'

# # Printing the updated dictionary
# print(my_dict)

# # QUESTION NO # 4
# def sum_numeric_values(dictionary):
#     total_sum = 0
#     for value in dictionary.values():
#         if isinstance(value, (int, float)):
#             total_sum += value
#     return total_sum

# # Example dictionary
# my_dict = {'a': 10, 'b': 5.5, 'c': 'apple', 'd': 7, 'e': 'banana'}

# result = sum_numeric_values(my_dict)
# print("Sum of numeric values:", result)

# # QUESTION NO # 5
# def find_duplicate_values(lst):
#     duplicates = []
#     for item in lst:
#         if lst.count(item) > 1 and item not in duplicates:
#             duplicates.append(item)
#     return duplicates

# # Example list
# my_list = [1, 2, 3, 2, 4, 3, 5, 6, 5, 7]

# duplicate_values = find_duplicate_values(my_list)
# print("Duplicate values:", duplicate_values)

# # QUESTION NO # 6
# def key_exists(dictionary, key):
#     return key in dictionary

# # Example dictionary
# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# key_to_check = 'age'

# if key_exists(my_dict, key_to_check):
#     print(f"The key '{key_to_check}' exists in the dictionary.")
# else:
#     print(f"The key '{key_to_check}' does not exist in the dictionary.")

