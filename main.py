
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


# name = input("hwat is your name: ")
# print("hello "+name)
# type(name)

# hour = int(input("how long have you worked: "))
# pay_for_hour = int(input("how much is your pay per hour: "))

# payment = (hour * pay_for_hour)
# print(payment)


# width = 17
# width = 12.0

# result_floor_division = width // 2  
# result_true_division = width / 2.0 

# print(type(result_floor_division))
# print(type(result_true_division))


# result = 1+2*5
# print(result)
# print(type(result))


# celsius = int(input("please give me the celsius: "))
# farenheit = (celsius * (9/5)+32)
# print(farenheit)

# result = 10 ** 9
# print(result)

# numbers = int(input("Put your "))

# def number_to_byte_converter(number):
#     try:
#         # Convert the number to its binary representation
#         binary_representation = bin(number)

#         # Remove the '0b' prefix from the binary string
#         binary_string = binary_representation[2:]

#         # Pad the binary string with leading zeros to make it a multiple of 8
#         padded_binary_string = binary_string.zfill((len(binary_string) + 7) // 8 * 8)

#         # Convert the binary string to bytes
#         byte_representation = bytes.fromhex(format(int(padded_binary_string, 2), 'x'))

#         return byte_representation
#     except ValueError as e:
#         return f"Error: {e}"

# # Example usage:
# value_for_conversion = int(input("Enter a number: "))
# result = number_to_byte_converter(value_for_conversion)
# print(f"Byte representation: {result}")



# def decimal_to_binary(num):
#     # Using bin() to convert decimal to binary and removing the '0b' prefix
#     binary_representation = bin(num)[2:]
#     return binary_representation

# def main():
#     # Taking user input for the decimal number
#     decimal_number = int(input("Enter a decimal number: "))

#     # Calling the function to convert decimal to binary
#     binary_representation = decimal_to_binary(decimal_number)

#     # Displaying the result
#     print(f"The binary representation of {decimal_number} is: {binary_representation}")

# if __name__ == "__main__":
#     main()



