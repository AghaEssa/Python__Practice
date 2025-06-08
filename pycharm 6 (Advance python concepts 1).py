# ********************(Advance__python)********************
# concept_____(1)...........(walrus_operator:=)
# lista1=[12,2,55,89,2,282,82,2812,19,752,21]
# if (n1:= len(lista1))<10:
#     print(f"length is smaller : {n1}")
# else:
#     print(f"high length {n1}")


# concept_____(2)
# # val1:int =12
# # val2:int =33
# # tot :int =val1+val2
# # print ("Two num the sum is : ",tot)
# # aa :str="the name is :"
# # bb :chr='f'
# # cc :float =72.2
# #
# #
# # def funcccc(name:str)->str:
# #     return f"Your name is :{name}...."
# #
# # nam1=input("Enter your name:")
# # print (funcccc(nam1))
#
#
# from typing import List,Tuple,Dict,Union
#
# list22 : List[float] = [1.1,.2,22.1,544.33]
# print("The List is :",end=" ")
# for i in list22:
#     print (i," ",end="")
#
# tuple22 : Tuple[str,int,float]=("Agha",22,9.992)
# print("\n\nThe Tuple is :",end=" ")
# for i in tuple22:
#     print (i," , ",end="")
#
# dict22 : Dict[str,int]={"na1":89,"na2":78,"na3":24}
# print("\n\nThe Dict is :",end=" ")
# for i in dict22:
#     print (dict22[i]," ",end="")
# print ("\n",dict22)
#
# union22: Union[str,int,float]=983
# print ("\nThe Union is :",union22)
# union22="whatever"
# print("\n\nThe Union is :",union22)
# union22=78.2
# print("\n\nThe Union is :",union22)



# concept_____(3)..........(Match_case)
# def switches(num:int):
#     match num:
#         case 1:
#             print ("heloow")
#         case 2:
#             print("second choice ......")
#         case 3:
#             print("third choice ......")
#
# n=int(input("enter number:"))
# switches(n)




# concept_____(4)..........(Merge dictionary)
# dict1={1:"ddd",2:"bbb"}
# dict2={3:"dde",4:"bbbp"}
# merged =dict1|dict2
# print (merged,"\n")
#
# with (
#     open("file1.txt","r")as xx1,
#     open("file2.txt","r")as xx2
# ):



# concept_____(5)..........(Exceptional handling )
# 1)try__Except
try:
   n1=int(input("Enter the  number: "))
   print(f"You entered {n1}")
except  Exception as out:
    print(out)
print ("Checking typing ....")

# 2)try__except__except
# try:
#    n1=int(input("Enter the  number: "))
#    print(f"You entered {n1}")
# except  ValueError as ot:
#     print(ot)
# except  ZeroDivisionError as ot:
#     print(ot)
# except  Exception as out:
#     print(out)
#
# print ("Checking typing ....")

# 3)raise_exception
# n9=int(input("Enter num 1:"))
# n8=int(input("Enter num 2:"))
# if n8==0:
#     raise ZeroDivisionError("num 2 is not suppose to  zero yahh.....  ")
# else :
#     print(F"After division :{n9/n8}")

# 4)try__except__else
# try:
#     n1=int(input("Enter the  number: "))
#     print(f"You entered {n1}")
# except  Exception as out:
#     print(out)
# else :   #run with try......only
#     print ("Checking typing ....")

# 5)try__finally
"""try:
    n1=int(input("Enter the  number: "))
    print(f"You entered {n1}")
except  Exception as out:
    print(out)
finally:  #work with both.................
    print ("i am finally")
"""
# or
"""
def finally_fun():
    try:
        n1 = int(input("Enter the  number: "))
        return f"You entered {n1}"
    except  Exception as out:
        return out
    finally:  # work with both.................
        print("i am finally")
print (finally_fun())
"""




# concept_____(6)..........( )
# from py_module_1 import fucc




# Global variable.............
"""a=2
def gun():
    a:int =11
    print(a)
gun()"""
# or
"""a=2
def gun():
    print(a)
gun()
"""
# or
"""a=2
def gun():
    global a
    a=99
    print(a)
gun()
print(a)"""



# enumerate................easyyyy
"""

l1=[732,39,338,283]
for item,index in enumerate(l1):
    print(f"value at {item}  is : {index}")
    
"""


# list comprehension......easy way....
"""li1=[1,2,3,4,5]                        #list_1
li2=[index*index for index in li1]     #list_2 is made from list_1
print(li2)

# copying list_1
li1=[1,2,3,4,5]                        
li2=[index for index in li1]
print(li2)
"""




# ................................( Project Number : 15 ).......................................
# 1)
# try:
#     with open("3 Essa.txt","r") as aa:
#         vn1=aa.readlines()
#         print ("3_txt_file_readed")
# except FileNotFoundError as xx12:
#     print(xx12)
# try:
#     with open("4 Essa.txt","r") as aa:
#         vn1=aa.readlines()
#         print ("4_txt_file_readed")
# except FileNotFoundError as xx12:
#     print(xx12)
# try:
#     with open("5 Essa.txt","r") as aa:
#         vn1=aa.readlines()
#         print ("5_txt_file_readed")
# except FileNotFoundError as xx12:
#     print(xx12)
#
# print ("working functionally")


# 2)
# n1=int(input("Enter the  number: "))
# lis12=[f"{n1} X {i} ={i*n1}" for i in range (1,11)]
# print(lis12)
# with open("6 Essa.txt","a") as fx:
#     fx.writelines(f"Table of {n1} is :{lis12}\n")


# 3)
# liss22=[1,2,3,4,5,6,7,8]
# for index,item in enumerate(liss22):
#     if item%2!=0:
#         if item!=1:
#             print(item)
#


# 4)
# try :
#     n1=int(input("Enter the  number 1: "))
#     n2=int(input("Enter the  number 2: "))
#     print("divide :",n1/n2)
# except ZeroDivisionError as etrr:
#     print(etrr,"IS NOT SUPPORTED")
# else :
#     print ("program not crashed .....ok")



# ................................(    Project End     ).......................................





















