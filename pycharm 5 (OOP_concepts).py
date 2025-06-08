class employe:
    id =""
    language=""
    salary=0
    def __init__(self,name ,id,language,salary):
        self.name =name
        self.id=id
        self.language=language
        self.salary=salary
    def printer(self):
        print(f"Person name is {self.name} & id is {self.id} \n language is {self.language} & salary is {self.salary}")
    @staticmethod
    def show ( ):
        print ("the end ",22)


E1=employe("Agha Essa","f202gs82","javascript",999100)
E1.name ="Essa"
E1.printer()
E1.show()



# ................................( Project Number : 13 ).......................................
# 1)
# class good:
#     num =12
#     def g1(sgh):
#         print (f"your num is {sgh.num}")
#
# aa1=good()
# aa1.g1()
# aa1.num=123
# aa1.g1()
# print (good.num)


# 2)
# class train_buy:
#     item_num=112
#     def __init__(self,name,seat_num):
#         self.name=name
#         self.seat_num=seat_num
#     def booking(self,rs):
#         print (f"{self.name} your  booking seat coast  is {rs*100} at item num {self.item_num}")
#     def location(self,time):
#         print (f"{self.name} your location is {self.seat_num} seat and train start at {time}o'clock")
#     @staticmethod
#     def great():
#         print ("hellow greating to you have a nice day Sir....!")
#
# nam1=input("Enter your first name:")
# seat1=int (input("Enter your seat number:"))
# BT1=train_buy(nam1,seat1)
# BT1.great()
# RS=int(input("Enter num of passengers :"))
# BT1.booking(RS)
# BT1.location(12)
# BT1.great()




# ................................(    Project End     ).......................................

# class employ:
# #     def __init__(self,name,age,salary):
# #         self.name=name
# #         self.age=age
# #         self.salary=salary
# #         print (f"{self.name} Employee is here now...")
# #     def info(self):
# #         print(f"Name: {self.name}")
# #         print(f"Age: {self.age}")
# #         print(f"Salary: {self.salary}")
# #
# # class manager:
# #     requirements="all"
# #     def __init__(self):
# #         print ("manager is now")
# #     @staticmethod
# #     def greeting():
# #         print("Welcome Sir...!")
# #     @classmethod
# #     def req(cls):
# #         print (f"MANAGER REQUIREMENTS is {cls.requirements} sure...!")
# #
# # class Boss (employ,manager):
# #     boss ="Boss22"
# #     def __init__(self):
# #         print ("Boss is now")
# #     def start(self ):
# #         print (f"Metting started by {self.boss}")
# #
# #
# # e1=employ("agha",2,22111)
# # e1.info()
# # m1=manager()
# # m1.greeting()
# # m1.req()
# # b1=Boss()
# # b1.start()
# # b1.greeting()




# class e1:
#     def __init__(self):
#         print ("e1 is here...")
#
#
# class e2(e1):
#     def __init__(self):
#         super().__init__()
#         print ("e2 is here...")
#
# class e3( e2):
#     def __init__(self):
#         super().__init__()
#         print ("e3 is here...")
#
#
# person1=e3()





# class alll:
#     def __init__(self,name):
#         self.name = name
#         print (f"{self.name} is ready here...")
#     @property
#     def st_lenghtss(self):
#         print (f"First word of line is \"{self.f_w}\" and Last word is \"{self.l_w}\"" )
#     @st_lenghtss.setter
#     def st_lenghtss(self,liness):
#         self.f_w=liness.split(" ")[0]
#         self.l_w=liness.split(" ")[2]
#
#
# p1=alll("Agha")
# p1.st_lenghtss="my fihsj aghakl"
# print(p1.st_lenghtss)






# class val:
#     def __init__(self,nn):
#         self.nn=nn
#     def __add__(self,va22):
#         return self.nn+va22.nn
#     def __sub__(self,va22):
#         return self.nn-va22.nn
#     def __mul__(self,va22):
#         return self.nn*va22.nn
#     def __truediv__(self,va22):
#         return self.nn/va22.nn
#     def __floordiv__(self,va22):
#         return self.nn//va22.nn
#
# p1=val(8)
# p2=val(2)
#
# print (f"sum of two obj is :{p1+p2}")
# print (f"minus of two obj is :{p1-p2}")
# print (f"divid  of two obj is :{p1/p2}")
# print (f"multpy of two obj is :{p1*p2}")
# print (f"floordivision of two obj is :{p1//p2}")







# .......................chatgpt.........................
# class MyObject:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return MyObject(self.value + other.value)
#
#     def __repr__(self):
#         return f"MyObject({self.value})"
#
# obj1 = MyObject(10)
# obj2 = MyObject(20)
# obj3 = MyObject(30)
# result = obj1 + obj2 + obj3
# print(result)  # Output: MyObject(60)





# ................................( Project Number : 14 ).......................................
# 1)
# class sparrow:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def show1(self):
#         print(f"Algebra :({self.a}i,{self.b}j)")
#
# class sparrow2(sparrow):
#     def __init__(self,a,b,c):
#         super().__init__(a,b)
#         self.c=c
#     def show2(self):
#         print(f"Algebra :({self.a}i,{self.b}j,{self.c}k)")
#
#
# p1=sparrow(3,4)
# p1.show1()
# p2=sparrow2(1,4,9)
# p2.show2()
# p2.show1()





# 2)
# class Animal:
#     pass
# class pet(Animal) :
#     pass
# class dog(pet) :
#     @staticmethod
#     def speak():
#         print("Bark bark")
#
# p1=dog()
# p1.speak()





# 3)
# class employ:
#     def __init__(self,salary,increment):
#         self.salary = salary
#         self.increment = increment
#     @property
#     def sal_aft_increase(self):
#         return f"Salary after increment :{((self.salary+self.salary) * self.increment):.1f}"
#
#     @sal_aft_increase.setter
#     def sal_aft_increase(self,value):
#         self.increment =((value/self.salary)-1)*100
#
# sal=int (input("Enter your salary:"))
# inc=int (input("Enter your increment:"))
# e1=employ(sal,inc)
#
# print (e1.sal_aft_increase)
# e1.sal_aft_increase=890000
# print(e1.increment)
# print (e1.sal_aft_increase)


# 4)
# class vendor :
#     def __init__(self, a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def __add__(self, other):
#         return vendor (self.a+other.a ,self.b+other.b,self.c+other.c)
#
#     def __mul__(self, other):
#         return vendor (self.a*other.a,self.b*other.b,self.c*other.c)
#
#     def __str__(self):
#         return  f"the valuesss add is : {self.a}i, {self.b}j, {self.c}k"
#
#
# person1=vendor (1,2,3)
# person2=vendor (2,2,2)
# print (person1+person2)
# print (f"after multiply the value is : {person1*person2}")



# 5)
# class lited:
#     def __init__(self,lit):
#         self.lit = lit
#     def __len__(self):
#         return len (self.lit)
#
#
# person1=lited([2,3,3,"hssh"])
# print(len (person1))


# ................................(    Project End     ).......................................











































