# Assignment No. 1
# Question 1
# Write a python program to print the following string in a spexcific format.

# print ("Twinkle, Twinkle, Little star\n\tHow I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\n Twinkle, Twinkle, Little star\n\tHow I wonder what you are ")

# """""
# python version(Question 2)
# """""
# import sys
# print("System Version")
# print (sys.version)


# Write a python program to display the current date and time.

# import datetime
# tod = datetime.datetime.now()
# print(tod)


# Area of a circle (Question 4)

# radius = float(input("Enter the Radius of Circle:"))
# A = 3.147* radius * radius
# print ("Area of Circel is:" ,A)


# Write a python program which tskes two inputs from user and print them addition
# num1 = int(input("Enter the First number:"))
# num2 = int(input("Enter the Second number:"))
# sum = (num1 + num2)
# print ("the Sum of two number is:" ,sum)

# write a program which take input from user and identify that the given numberis even or odd.
# num_1 = int (input ("Enter the number: "))
# print (num_1 % 2)
# if (num_1 % 2 ==0):
#     print (num_1, "is even number")
# else: 
#     print (num_1, "is odd number")

# write a python program which accept the user's forst and last name and print them in reverse order with a space between them.
# F_name = input ("Enter First Name: ")
# L_name = input ("Enter last name: ")
# print (L_name +" "+ F_name)

# Write a program ehich takes five input from user for different subject's makrs, total it and genrate marksheet using grades.

# Student_name = input("Enter Student Name: ")
# Roll_number =  int (input ("Enter Roll number: "))
# Standard = int (input ("Enter Standard: "))   
# English = int (input ("Enter English Marks: ")) 
# Math = int (input ("Enter Math Marks: ")) 
# Islamiat = int (input ("Enter Islamiat Mark: ")) 
# Physic = int(input("Enter Physic Marks: "))
# Chemistry = int(input("Enter Chemistry Marks: "))
# Marks_Obtained = English + Math + Islamiat + Physic + Chemistry
# print (Marks_Obtained)
# Total_Marks = 500
# perc = (Marks_Obtained / Total_Marks)*100
# print (perc)
# if perc <=100 and perc >= 90:
#     print("Grade: A+")
# elif perc <=90 and perc >=80:
#     print("Grade: A")
# elif perc <=80 and perc >=70:
#     print("Grade: B+")
# elif perc <=70 and perc >=60:
#     print("Grade: B")
# elif perc <= 60 and perc >=50:
#     print("Grade: C+")
# elif perc <=50 and perc >=40:
#     print("Grade:D (Fail)")
# elif perc <100 or perc > 50:
#     print ("Put the correct grade")
# else:
#     print ("Result: Fail")

# 9. Write a program which print the length of the list?
# l1 = ["hammna","hira","Fatima",34,25,2.0,True]
# len_of_l1 = len(l1)
# print("length of list is :" , str(len_of_l1))

#10.Write a Python program to sum all the numeric items in a list?
# def sum_list(lst):
#     sum_numbers = 0
#     for item in lst:
#         if isinstance(item,(int,float)):
#             sum_numbers += item
#     return sum_numbers
# my_list = ["hammna","hira","Fatima",34,25,2.0,True]
# total_sum = sum_list(my_list)
# print(total_sum)

# 11.Write a Python program to get the largest number from a numeric list.
# l2 = [5,8,9,55,200,25000]
# l2.sort()
# print("Largest number in the list is:"+ str(l2[-1]))

# 12. Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Write a program that prints out all the elements of the list that are less than 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for element in a:
#     if element < 5:
#         print(f'{element}')

# 1. Make a calculator using Python with addition , subtraction ,multiplication ,division and power.
# val1 = int(input("lease put valuse 1:"))
# val2 = int(input("Please put valuse 2:"))
# val3 = input("Please type operate:")
# sum = val1 +val2
# sub = val1- val2
# mul = val1 * val2
# div = val1 / val2
# if(val3 == "+"):
#     print("Your Answer is:"+ str(sum))
# elif(val3 == "-"):
#     print("Your Answer is:"+ str(sub))
# elif(val3 == "*"):
#     print("Your Answer is:"+ str(mul))
# elif(val3 == "/"):
#     print("Your Answer is:"+ str(div))
# else:
#     print("You put wrong operator")

# Write a program to check if there is any numeric value in list using for loop.

# def has_num_value(lst):
#     for item in lst:
#         if isinstance(item,(int,float)):
#             return True
#     return False
# my_list = ['1','Hamna', 'hira']
# result = has_num_value(my_list)
# if result:
#     print("In list there is numeric value exist")
# else:
#     print("No numberic value exist")

# Write a Python script to add a key to a dictionary.
# my_dict = {
#     "Name": "Hammna","Age":25 , "City":"Karachi"
# }
# my_dict["Education"]="Engineer"
# print (f'Updated Dictionary:',my_dict)

# Write a Python program to sum all the numeric items in a dictionary.
# def num_my_dict(dictionary):
#     sum = 0
#     for val in dictionary.values():
#         if isinstance(val,(int,float)):
#             sum += val
#     return sum
# my_dict = {"a":10, "b":"3.14","c":7, "d":89, "e":"not-numeric"}
# sum_my_dict = num_my_dict(my_dict)
# print(f'Sum of Numeric value is',sum_my_dict)

# Write a program to identify duplicate values from list.
# l1 =[1,1,3,4,5,6,8,3,9,5]
# dup_l1 =[]
# for i in l1:
#     if i not in dup_l1:
#         dup_l1.append(i)
#     else:
#         print(i,end=' ')

# Write a Python script to check if a given key already exists in a dictionary
# def is_key_present(dic,key):
#     if key in dic.keys():
#         print("Key is presence in dictionary")
#     else:
#         print("key is not presence in dictionary")
# mydict = {"Name": "hammna","Age": 25 ,"City":"Karachi"}
# key = 'name'
# is_key_present(mydict,key)

