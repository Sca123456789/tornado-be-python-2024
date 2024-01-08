# def f(a, b, z):
#     # add = (a*a) + (b*b)
#     # add = (a*a) - (2*a*b)+ (b*b)
#     add = (a*a) + (b*b)
#     return add
# x = f(10, 20,30)
# print(x)

# import math

# def sum_of_squares(numbers):
#     return sum(x**2 for x in numbers)

# numbers = [1, 2, 3, 4, 5]
# result = sum_of_squares(numbers)
# print(f"The sum of the squares is: {result}")

# def calculate_statistics(numbers):
#     total = sum(numbers)
#     count = len(numbers)
#     average = total / count if count > 0 else 0
#     return total, count, average

# def main():
#     entered_numbers = []

#     while True:
#         try:
#             user_input = input("Enter a number (type 'done' to finish): ")
            
#             if user_input.lower() == 'done':
#                 break  
            
#             number = float(user_input)
#             entered_numbers.append(number)

#         except ValueError as e:
#             print(f"Error: {e}. Please enter a valid number.")

#     try:
#         total, count, average = calculate_statistics(entered_numbers)
#         print(f"\nSum: {total}\nCount: {count}\nAverage: {average:.2f}")
#     except ZeroDivisionError:
#         print("No numbers entered.")

# if __name__ == "__main__":
#     main()
