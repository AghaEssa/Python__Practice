# def cal(turns):
#     sum =0
#     for i in range (1,turns+1):
#         n1=int (input (f"Enter num {i} : "))
#         sum+=n1
#     return sum
#
# def cal2(sumss, itvalue):
#     average=sumss/itvalue
#     return average
#
# v1=int (input("Enter iterations num : "))
# output=cal(v1)
# print(f"Your Sum value is : {output}")
# avg=cal2(output,v1)
# print (f"your average is : {avg}")
from os import remove


# ................................( Project Number : 11 ).......................................

# 1)
# def entry():
#      n1=int (input ("Enter num 1: "))
#      n2=int (input ("Enter num 2: "))
#      n3=int (input ("Enter num 3: "))
#      if n1>n2 and n1>n3:
#          return n1
#      elif n2>n1 and n2>n3:
#          return n2
#      elif n3>n1 and n3>n2:
#          return n3
#
# print (f'Highest num is : {entry()}')

# 2)
# def f_c(req):
#     c=5*(req-32)/9
#     return c
#
# n1=int (input ("enter num : "))
# kl=f_c(n1)
# print (f"today temp is {round(kl,1)} *C")

# 3)
# def nat(v1):
#     if v1==0:
#         return 0
#     vv=v1-1
#     return nat(vv)+v1
# m=int (input("enter the number:"))
# bb=nat(m)
# print ("sum =",bb)

# 4)
# def star (n):
#     if (n==0):
#         return " "
#     print (f"{"*  "*n} ")
#     star(n-1)
#
# n1=int (input("Enter a number: "))
# star(n1)

# 5)
# def cuts(listdd,cutu):
#     nt=[]
#     for items in listdd:
#         if (not (items==cutu)):
#             nt.append(items.split(cutu))
#
#     return nt
#
# listdd=["Essa","farnsa","sa","sale","tahsa","112"]
# print (cuts(listdd,"sa"))


# ................................(    Project End     ).......................................

# def priy(ddf):
#     print ("\n\n\n")
#     for i in ddf:
#         print (f"Fruit {i} :{ddf[i]} \n ")
#
# n1=int (input("Enter a numbers of fruit : "))
# dict={}
# for i in range (1,1+n1):
#     dict[i]=i=input("Enter a fruit : ")
# priy(dict)





















