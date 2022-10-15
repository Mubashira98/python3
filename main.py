# def first(first_v):
#     print(first_v+"hi")
# first("mubashira")

# def my_fun(fname,lname):
#     print(fname + "is" + lname)
# my_fun("India","beautiful")

# def my_function(*names):
#     print("beautiful child is" + names[1])
# my_function("ab","cd","ef","abcd",'fgh')

# def my_fun(child2,child3,child1):
#     print("eldest child is "+ child1)
# my_fun(child1="abinav",child2="akshay",child3="anju")

# def my_fun(**names):
#     print("last name is "+ names["lname"])
#
# my_fun(fname="arun",lname="ajith")

# def is_palindrome(word):
#     if word==word[::-1]:
#         print("palindrome")
#     else:
#         print("not palindrome")
# is_palindrome(input())


# n=int(input("enter number of transactions:"))
# amount=0
# l=[]
# for i in range(1,n):
#     value=input("enter amount")
#     l.append(value)
# print(l)
# for x in l:
#     s = int(x[1:])
#     if x[0]=="D":
#         amount=amount+s
#     else:
#         amount=amount-s
# print(amount)
#
# --------------
# Define a function that can accept two strings as input and print the string with maximum length
# in console.If two strings have the same length, then the function should print al l strings line by line.
# def max_len(string_1,string_2):
#     if len(string_1)>len(string_2):
#         print(string_1)
#     elif len(string_1)==len(string_2):
#         print(string_1)
#         print(string_2)
#     else:
#         print(string_2)
# max_len(input(),input())
# ----------------------------------------

"""
 Define a function which can print a dictionary where the keys are numbers between
 1 and 20 (both included) and the values are square of keys.
 {1:1,2:4,3:9,4:16 ........}
 """

dict={}
def my_dict():
    for i in range(1,21):
        dict.__setitem__(i,i**2)
    return dict
print(my_dict())








