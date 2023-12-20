# x = 1
# y = 1



# print(x == y)
# print(x >= y)

# print(x is not y)

# print(x is y)


# age  = int(input("how old are you: "))
# print( age)
# if age <= 12 and age >=1: 
#     print("you are a child")
# elif age <= 19 and age >= 13:
#     print(" you are a teen")
# elif age <= 59 and age >= 20:
#     print("I think you are a adult")
# elif age<= 100 and age >= 60:
#     print("ypu ar e na old man")       
# else:
#     print("you are a dinasour")


# def age_test():
#     print("hello world")

# def learn_to_code():
#     if 20 <= age <= 40:
#         print(" you are a old dirty dog")

# learn_to_code()


def salary():
    salary = 10
    hours_worked = int(input("hwo long did you worked: "))
    result = ((hours_worked - 40) * 15 + (40 * 10))
    if 40 < hours_worked:
        print(result)
salary()