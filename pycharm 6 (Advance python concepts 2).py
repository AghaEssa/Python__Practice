# ********************(Advance__python)********************
# concept_____(1)...........(lambda)
sqr_fun=lambda a: a*a
n1=int(input("Enter number: "))
print(f"your square is :{sqr_fun(n1)}")

sum_fun=lambda a,b,c : a+b+c
n2=int(input("Enter 1 number: "))
n3=int(input("Enter 2 number: "))
n4=int(input("Enter 3 number: "))
print(f"Your Sum is {sum_fun(n2,n3,n4)}")




# concept_____(2)...........(join method )
# klist=["apple","dah","uaa"]
# valt="_".join(klist)
# print(valt)





# concept_____(3)...........(Map,filter & reduce  )
# map
# alist=[1,2,3,4,5]
# num_s=lambda x:x*x
# square_list=map(num_s,alist)
# print(list(square_list))


# filter
# listq=[2,34]
# def even_sort(xn):
#     if xn%2==0:
#         return True
#     return  False
# ff=filter(even_sort,listq)
# print(list(ff))
#
# tempk2 :None
# for index, item in enumerate(ff):
#     tempk2 = item
#     break
#
# print (tempk2,"essa fetch xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# reduce
# from functools import reduce
# klist=[1,2,3,4,5]
# sums=lambda a,b:a+b
# reduce_fg=reduce(sums,klist)
# print(reduce_fg)



# .........Practice set
# 1)
# n=input("Enter yur name :")
# n1=int (input("Enter your age :"))
# id =input("Enter your id :")
#
# print ("your name is {} and age is {} and id is {}.".format(n,n1,id))


# 2)
# tabs=[f"5X{i}={i*5}" for i in range(1,11)]
# e1="\n".join(tabs)
# print(e1)


# 3)
# li=[11,55,5,35,2828]
# def check(a):
#      if a%5==0:
#          return True
#      return False
#
# sx=filter(check,li)
# print(list(sx))


# 4)
# from functools import reduce
# flist=[23,4,5,657,882392382,68,544,323,212]
#
# def hi(a,d):
#     if a>d:
#         return a
#     return d
#
# wet=reduce(hi,flist)
# print(wet)


# 5)
# mobile web page...create
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World</p>"
#
# app.run()

# l1=[11,26,3,74,5,96,7,88,9,10]
# num :int=0
# for index,item in enumerate(l1):
#     num+=item
#     print(f"value at {index+1}  is : {item}")
#
# print(f"sum of 10 is {num}")


# val:int =0
# for index in range(1,11):
#    print(index)
#    val+=index
#
#
# print(val)






















