#................................Tuples
# aa=(22,62,2,"sdhsd",'d','ds',93)
# bb=(22,)
# print(aa)
# print(type(aa))
# print(type(bb))   # type found
# print(aa[1])

# ........................
# # counting perticular value in tuple
# ac=("gsh",22,3,34,0,332,22,22,2,22)
# print ("22 count is: ", ac.count(22))
# # value present at index
# num=ac.index(332)
# print ("value present at index :", num)


# ................................( Project Number : 8 ).......................................
# 1 )
# listd=[]
# va1=(input("Enter car name :"))
# listd.append(va1)
# va1=(input("Enter car name :"))
# listd.append(va1)
# va1=(input("Enter car name :"))
# listd.append(va1)
# va1=(input("Enter car name :"))
# listd.append(va1)
# va1=(input("Enter car name :"))
# listd.append(va1)
#
# print(listd)


# 2 )
# arraylist=[]
# va1=int(input("Enter Your Marks here :"))
# arraylist.append(va1)
# va1=int(input("Enter Your Marks here :"))
# arraylist.append(va1)
# va1=int(input("Enter Your Marks here :"))
# arraylist.append(va1)
# va1=int(input("Enter Your Marks here :"))
# arraylist.append(va1)
# va1=int(input("Enter Your Marks here :"))
# arraylist.append(va1)
#
# print(arraylist)
# arraylist.sort()
# print (arraylist)
#
# # 3 ) sum function used
# total1=sum(arraylist)
# print ("Sum of all values will be : ",total1)


# 4)
# asd=(5,"hh","ygs",22,6432,8,8,8,8)
# essa=asd.count(8)
# print(essa)


# ................................(    Project End     ).......................................


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# .............................Dictionarys & Methods...................^^^^^
# Essa_Dictionary={
#
#     "Essa" :100,
#     "Moosa":101,
#     "Hamza":83,
#      'g'   :"soona",
#       4.1  :"agaaa",
#        11  :'gg'
#
# }
# print("Its data type is : ",type(Essa_Dictionary),"\n")
# print (Essa_Dictionary,"\n")
# print (Essa_Dictionary["Essa"])
# print(Essa_Dictionary[4.1])
# Essa_Dictionary[4.1]="Agha_Essa_Khan"   #changing  values  ......
# print(Essa_Dictionary,"\n","\n")
# # ............................................................................


"""

#...........................(Starts its Method).............................now
# 1) printing all keys.......1
print (Essa_Dictionary.keys())

# 2) printing all values.......2
print (Essa_Dictionary.values())

# 3) printing all items of dictionary ok .......3
print (Essa_Dictionary.items())

# 4) updating and adding values  ok .......4
Essa_Dictionary.update({"Essa":1000,"hassam":10010,'lays':52,11:"Wrong one"})
print(Essa_Dictionary)
print (Essa_Dictionary.items(),"\n")

# 5) get method.......5
print (Essa_Dictionary.get("hassam"))
print (Essa_Dictionary.get("salee"))
print (Essa_Dictionary["hassam"])



# *****************************************************************************************

"""

#
# # ..............................(Sets in python)...................
#
# # 1) set
# num22={1,2,3,"essa",2,'g',7,2,9.1}  # Set
# print (type(num22))
# print (num22)
#
# # 2) Empty set
# num23=set()              #Empty set
# print (type(num23))
# print (num23)
#
#
# # .................Methods in set
# # 3) add in set
# num22.add("add99")
# print (num22)
#
# # 4) remove in set
# num22.remove(9.1)
# print (num22)
#
# # 5) clear in set
# num22.clear()
# print (num22)
# # ....
# num22.add("hxx")
# print (num22)
#
# # 6) union in set
# set1={1,3,45}
# set2={66,1,44,3,45}
# print("Union of above sets : ",set1.union(set2))
#
# # 7) intersection in set
# print ("Intersection of above sets : ",set1.intersection(set2))
#
# # 8) Subset in set
# print ("set1 is a Subset of  set2 :",set1.issubset(set2))
#




# ................................( Project Number : 9 ).......................................
#
# # 1)
# dicts={
#     "madat":"help",
#     "salee":"bahi"
# }
# word=input("enter :")
# print(dicts[word])

# 2)
# dset1=set()
# vomer=int (input("enter num :"))
# dset1.add(vomer)
# vomer=int (input("enter num :"))
# dset1.add(vomer)
# vomer=int (input("enter num :"))
# dset1.add(vomer)
# vomer=int (input("enter num :"))
# dset1.add(vomer)
# vomer=int (input("enter num :"))
# dset1.add(vomer)
# vomer=int (input("enter num :"))
# dset1.add(vomer)
# vomer=int (input("enter num :"))
# dset1.add(vomer)
# print ("all num :",dset1)

# # 3)
# set44={2}
# set44.add(2.0)
# set44.add(12)
# set44.add('2')
# print ("all numbers :",set44)
#
# # 4)
# s={}   #dictionary type

# 5)
# doctinary={}
# dat1=input("Enter your name :")
# descr1=input("Enter your car :")
# doctinary.update({dat1:descr1})
# dat1=input("Enter your name :")
# descr1=input("Enter your car :")
# doctinary.update({dat1:descr1})
# dat1=input("Enter your name :")
# descr1=input("Enter your car :")
# doctinary.update({dat1:descr1})
# dat1=input("Enter your name :")
# descr1=input("Enter your car :")
# doctinary.update({dat1:descr1})
# dat1=input("Enter your name :")
# descr1=input("Enter your car :")
# doctinary.update({dat1:descr1})
# print (doctinary)


# ................................(    Project End     ).......................................


# .................if_elif_else............................
# data1=input("Enter your password :")
# if (data1=="1agha"):
#     print("Correct one entered....")
# elif (data1=="2agha"):
#     print("wrong one entered....")
# elif (data1=="123"):
#     print("invalid")
# elif (data1=="-123"):
#     print("minus")
# elif (data1=="0.1"):
#     print("float")
# else:
#     print("Abey_Saleee")



# ................................( Project Number : 9 ).......................................

# 1)
# v1=int (input ("Enter num 1 :"))
# v2=int (input ("Enter num 2 :"))
# v3=int (input ("Enter num 3 :"))
#
# if(v1>v2 and v1>v3):
#     print (v1,"is greater.")
# elif(v2>v1 and v2>v3):
#     print (v2,"is greater.")
# elif(v3>v2 and v3>v1):
#     print (v3,"is greater.")

# 2)
# sub1=int (input("Enter first Subject number: "))
# sub2=int (input("Enter Second Subject number: "))
# sub3=int (input("Enter third Subject number: "))
# total_percentage=((sub1+sub2+sub3)/300)*100
# if(total_percentage>=40 and sub1>=30 and sub2>=30 and sub3>=30):
#     print ("You are passed ",total_percentage)
# else:
#     print ("You are not passed ",total_percentage)

# 3)
# l1="spam"
# l2="eggs"
# l3="do like me"
# l4="follow me"
# comt=input("Enter your comment : ")
# if(l1 in comt or  l2 in comt or  l3 in comt or  l4 in comt ):
#     print ("spamer haa")
# else:
#     print ("not")

# 4)
# post=input("Enter your post : ")
# if ("Essa".lower() in post.lower()):
#     print ("Ha ji ha present ")
# else :
#     print ("nahi ha ")

# ................................(    Project End     ).......................................



# ************( While_loop,For_loop,For_else_loop,pass_statement)*************************

for ax in range(0,5):
    print (ax)
    print ("\t")

for ax1 in range(6):
    print (ax1)
# else:
#     print ("done all")
# print ("\n")
#
#
# list12=["agha",123,"gah",'fg',2.2,"fan"]
# d1=0
# for ax3 in range(d1,len(list12)):
#     print(list12[d1])
#     d1+=1
#
# #     pass statement
# for i in range(100):
#     pass
#
#
#
# v1=0
# while (v1 <= 4) :
#     print(v1)
#     v1+=1
# else:
#     print ("done done")
#
#
#
#
# tuple1222=(22,33,6,7,443,77,"jdjd",'dd')
# n1=0
# while (n1<len(tuple1222)):
#     print(tuple1222[n1])
#     n1+=1



# ................................( Project Number : 10 ).......................................

# # 1)
# n=int (input ("Enter any number :"))
# for i in range (1,11):
#     print (f"{n} X {i} = {n*i}")
#
# # 2)
# n=int (input ("Enter any number :"))
# for i in range (1,11):
#     print (f"{n} X {11-i} = {n*(11-i)}")

# 3)
# n=int (input ("Enter any number :"))
# for i in range (1,n+1):
#     print (f"{" "*(n-i)}{" * "*i}"  "")


# 4)
n=int (input ("Enter any number :"))
for i in range (1,n+1):
    if (i==1 or i==n):
        print (f"{"*"*n}")
    else:
        print(f"*{(" "*(n-2))}*")


# 5)
for i in range (1,5):
    print ("*"*i, end="" )
    print ("r",end="")
    print ("*")


# 6)
# list=["esa khan","hassam","Essa khan","lays","elisha xj"]
# for i in list :
#     if (i.lower().startswith("e")):
#         print(f"Welcome  {i.title()}")


# ................................(    Project End     ).......................................


