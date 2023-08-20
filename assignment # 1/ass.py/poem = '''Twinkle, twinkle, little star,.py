# # PYTHON PROGRAMMING LANGUAGE ASSIGNMENT

# # QUESTIO NO # 1
# poem = '''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
# Twinkle, twinkle, little star,
# How I wonder what you are'''

# print(poem)

# # QUESTION NO # 2
# import sys
# print("Python version:")
# print(sys.version)
# print("Version info:")
# print(sys.version_info)

# # QUESTION NO # 3
# import datetime
# current_datetime = datetime.datetime.now()

# print("current date and time:", current_datetime)

# # QUESTION NO # 4
# import math
# radius = float(input("Enter the radius of the circle: "))
# area = math.pi * radius ** 2

# print(f"The area of the circle with radius {radius} is {area:.2f}")

# # QUESTION NO # 5
# def print_reverse_name(first_name, last_name):
#     full_name = last_name + " " + first_name
#     print(full_name)

# user_first_name = input("Enter your first name: ")
# user_last_name = input("Enter your last name: ")

# print_reverse_name("aqsa", "kanwal")

# # QUESTION NO # 6
# def main():
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
    
#     addition = num1 + num2
#     print("The sum is:", addition)

# if  __name__  == "_main_":
#     main()

# # QUESTION NO # 7
# def calculate_grade(mark):
#     if mark >= 90:
#         return "A+"
#     elif mark >= 80:
#         return "A"
#     elif mark >= 70:
#         return "B"
#     elif mark >= 60:
#         return "C"
#     elif mark >= 50:
#         return "D"
#     else:
#         return "F"

# def main():
#     subject_marks = []
#     total_marks = 0
    
#     for i in range(5):
#         subject_mark = float(input(f"Enter marks for subject {i + 1}: "))
#         subject_marks.append(subject_mark)
#         total_marks += subject_mark
    
#     average_marks = total_marks / 5
#     grade = calculate_grade(average_marks)
    
#     print("\nMark Sheet:")
#     print("-------------")
#     for i in range(5):
#         print(f"Subject {i + 1}: {subject_marks[i]}")
#     print("Total Marks:", total_marks)
#     print("Average Marks:", average_marks)
#     print("Grade:", grade)

# if _name_ == "_main_":
#     main()

# # QUESTION NO # 8
# # Taking input from the user
# number = int(input("Enter a number: "))

# # Checking if the number is even or odd
# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")

# # QUESTION NO # 9
# my_list = [1, 2, 3, 4, 5]
# length = len(my_list)
# print("Length of the list:", length)

# QUESTION NO # 10
# def sum_numeric_items(input_list):
#     total = 0
#     for item in input_list:
#         if isinstance(item, (int, float)):
#             total += item
#     return total

# my_list = [1, 2, 3, 4.5, "not a number", 5.5]
# result = sum_numeric_items(my_list)
# print("Sum of numeric items:", result)

# # QUESTION NO # 11
# def find_largest_number(input_list):
#     if not input_list:
#         return None
    
#     largest = input_list[0]
#     for num in input_list:
#         if isinstance(num, (int, float)) and num > largest:
#             largest = num
#     return largest

# my_list = [10, 5, 25.5, 8, 15.7]
# largest_num = find_largest_number(my_list)

# if largest_num is not None:
#     print("The largest number:", largest_num)
# else:
#     print("The list is empty or contains no numeric values.")

# # QUESTION NO # 12
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# for element in a:
#     if element < 5:
#         print(element)

