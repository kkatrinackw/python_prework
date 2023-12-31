# # Question 1
# # Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

# def hello_name(user_name):
#     print("hello_" + user_name.upper() + "!")
# hello_name('stranger')


# # Question 2
# # Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

# def first_odds():
#     for num in range(1, 100):
#         if num %2 != 0:
#             print(num, end=" ")
# first_odds()


# # Question 3
# # Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

# def max_num_in_list(a_list):
#     max_num = max(a_list)
#     return (max_num)

# list = [83, 20, 12, 56, 62, 18, 67, 40, 53, 25, 31, 69, 66, 13, 89, 41, 72, 73, 6, 54]
# max_value = max_num_in_list(list)
# print(max_value)


# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

 
# def is_leap_year(a_year):
#    leap_num = int(a_year)
#    while a_year:
#        if leap_num %4 == 0 and leap_num %100 != 0:
#         return True
#        elif leap_num %400 == 0:
#           return True
#        else:
#           return False
       
# leap_num = 2000
# leap_value = is_leap_year(leap_num)
# print(leap_value)

# Comments: For the code of question 4:The use of a while loop is unnecessary and can be removed. Also check your indentation with the first return statement.
# You can mix the statements inside the 'if' and 'elif' for it to have a better syntax (this is optional but a good practice).
   
# after refctoring:
def is_leap_year(a_year):
   leap_num = int(a_year)
   if leap_num %4 == 0 and leap_num %100 != 0:
    return True
   elif leap_num %400 == 0:
    return True
   else:
    return False
       
leap_num = 2032
leap_value = is_leap_year(leap_num)
print(leap_value)
       

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.


# def is_consecutive(a_list):
#     previous_number = a_list[0]
#     for number in a_list[1:]:
#         if number != previous_number + 1:
#             return False
#         return True

# list_1 = [2, 3, 4, 5, 6, 7]
# list_2 = [1, 4, 5, 6, 7]

# print(is_consecutive(list_1)) 
# print(is_consecutive(list_2))

# Comments: For the code of question 5:
# Your code needs more work, for example try this list:  [2, 3, 6, 7,5],  it returns True and it happens because the function returns True as soon as it finds the first pair of non-consecutive numbers (2 and 3).  
# You are close to solving it but your 'for' loop needs refactoring.

# after refactoring:
def is_consecutive(a_list):
    previous_number = a_list[0]
    for number in a_list[1:]:
        if number != previous_number + 1:
            break
        previous_number = number
    else:
        return True
    return False

list_1 = [2, 3, 4, 5, 6, 7]
list_2 = [1, 4, 5, 6, 7]
list_3 = [2, 3, 4, 5, 7]

print(is_consecutive(list_1)) 
print(is_consecutive(list_2))
print(is_consecutive(list_3))
