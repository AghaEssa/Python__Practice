print("Open source dev")
var1 =12
var2 ="TEXT"
var3 =28.2
sentence  ="write"
age =19


var4 :int =26   #decleration and initialization



# make  input output
entry=int (input("enter your age :"))
print  (entry)




x = None  # if nothing assing to a variable
entry1 = input("enter your age :")    # it is also similar in this case where (entry1) variable is not assign yet and also not declear its type as well.
x = entry1
print(x)





# to show its data type
var5=12.2
print (type(var5))
var6="ddddd"
print (type(var6))
var7=12
print (type(var7))
var8=88+2j         #complex data type (new)
print (type(var8))




var8=88+2j         #complex data type (new) have two parts  one is real_part and other is imaginary_part. now how to show.
print(var8)
print (type(var8))
print(var8.real)   #show real part of complex number
print(var8.imag)   #show imaginary part of complex number



#type Casting in python............................................................................................

var9 = 12
print(var9)
print(f"var9 data_type  is :{type(var9)}")
var10 = str(var9)
print(var10)
print(f"var10 data_type  is :{type(var10)}")
# some details of type casting
# two type of type casting:
# 1)implicit type casting
# 2)explicit type casting

# 1)implicit type casting:
# ---> a)Integer to Float during arithmetic operations.
# ---> b)Integer to Complex when used with complex numbers.
# ---> Float to Complex when used with complex numbers.
# ---> String Operations:(Strings are concatenated when both operands are strings.)

# a)
a=True      #boolean type as in C++   (true=1)
b=13.4      #float
c=a+b
print(c)    #it add through type casting

# b)
a1=4.4
b1=7
c1=a1+b1
print(c1)

#*********************************************************************************************************
# 2)explicit type casting:
# Common functions for explicit conversion include int(), float(), str(), list(), tuple(), and set().

# int()
a = "12"
b = "3"
c = int(a) + int(b)    #convert string to the int type ....
print(c)

# b)
e1=int(a)    #now you convert string into int and then add e1+e2
e2=1
print(e1+e2)

# and more....


#--------------------------------------------------------------------------------------------------------

# replace function for string
num5="you are a good and good and good and  a  good person."
print (num5.replace('good','bad'))              # Replacings..............
print (num5.replace("a","yyx"))





#for loop in python............................................................................................
# 1)
lsit_new = [12, 45, 67, 22, 3]
for index in lsit_new:  # selcet index_elements one by one from list  and print  it
    print(index)


print("\n")    #for new_line like endl  in C++


# 2)  simple print 1---10 numbers
for i in range(1, 11):
    print(i)


# 3)
for a in range(6):
    print (a)


# 4)
list_agha=["agha",123,"gah",'fg',2.2,"fan"]

for index in list_agha:
    print  (  list_agha[index]  )

# if you want to find the full  length of the  list--> "list_agha" then you can find it by this
print ( f" the total length of the list_agha is  : {len(list_agha)}"  )






#while loop in python............................................................................................

# 1)
v1=1
while (v1 < 5) :
    print(v1)
    v1 =v1+1
else:           # when while loop is completed then else part is executed  ye wase he likha ha marzi ha...
    print ("while done done")


# 2)
tuple_new=(22,443,77,"jdjd",'dd')
n1=0
while ( n1 < len(tuple_new) ) :             # len(tuple_new)==5     ----->( 0 < 5 ) is this condition true ..?
    print(tuple_new[n1])
    n1=n1+1





#if elif else  in python............................................................................................
# 1)
a=18
b=17

if  a==b:
    print("a an b are equal.")
elif a < b :
    print("a is less than b")
elif a > b :
    print("a is greater than b")
else:
    print("any error.. may be")





# 2)
listr = [12, 45, 7, 4, 7]
a = 0
b = 1

while a != len(listr):  # len(listr)==5
    if listr[a] == 4:
        b = 11
        print("Match ho gya yr...")
    a = a + 1

if b == 1:
    print("Match nahi hoa  yr...")



#Task practice .....................................................................................................

# task #4
for i in range (0,11):
    print(i)



# task 1
num1= int(input("enter first number :"))
num2= int(input("enter second number :"))
sum=num1+num2
print(f"your sum is {sum}.")



# task #2
n1=str(input("enter your name :"))
n2=int(input("enter your age :"))
if n1 =="agha":
    print("Greetings Sir....")
else:
    print("I am not Greeting you (write name=agha )..........")




# task 3
num10 =4
print(num10 **2)      # taking square of the number
# another method
print ("another method of taking square")
print(num10 * num10)





# task 4
index = 0
while index != 11:
    if index % 2 == 0:
        print(f"{index} is even .")
    index = index + 1

print("even numbers from (1---10) are shown above.")





# task#5
n=int(input("enter a number :"))
if n==0:
    print("n is Zero.")
elif n>0:
    print(f"n is positive.")
else:
    print(f"n is negative.")






# sort the given list
list=[2222,21,22,1,478]
list.sort()   #print the list in sorted form ...
print ( list)





# task find the greater number  among from list
list = [111, 3, 473, 1]
a = 0
for index in list:
    if index > a:
        a = index

print(f" the greater number  from the above list is {a}.")



