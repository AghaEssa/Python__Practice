from dataclasses import replace
from os import write

# vase="ye print karwana ************"
# vasee="ye print karwana ************"
# vaseee="ye print karwana ************"
#
#
# a=open("1 Essa.txt","r")
# fet=a.read()
# print (fet)
# a.close()
#
#
# b=open("1 Essa.txt","w")
# b.write(vase+"\n" )
# b.write(vasee+"\n" )
# b.write(vaseee )
# b.close()
#
# c=open("1 Essa.txt","r")
# rtx=c.read()
# print ("\n\n\n")
# print (rtx)
# c.close()

# d=open("1 Essa.txt","r")
# vist=d.readline()
# while vist != "":
#     print (vist)
#     vist=d.readline()
# d.close()




# with open("1 Essa.txt") as df:
#     fag=df.readline()
#     while fag!="":
#         print (fag)
#         fag=df.readline()


# ................................( Project Number : 12 ).......................................
# 1)
# with open ("1 Essa.txt","r") as aa:
#     content = aa.read()
#     if content=="":
#         print (f"The content is empty right now...")
#     else :
#         print ("The content is filled...")

# 2)
# with open ("1 Essa.txt","r") as aa :
#     content = aa.read()
#
# with open("2 Essa.txt","w") as bb :
#     bb.write(content)

# 3)
# with open ("1 Essa.txt", "r")as aa:
#     content1=aa.readlines()
#
# with open ("2 Essa.txt", "r")as bb:
#     content2=bb.readlines()
#
# if content1==content2:
#     print ("Both Files have same content...")
# else:
#     print("both Files have different content...")


# 4)
# def Table_printer(ixy):
#     stable=""
#     for aa in range (1,11):
#          stable+=f"{ixy} X {aa} = {ixy*aa}\n"
#
#     with open(f"file_E{ixy}.txt","w") as f:
#           f.write(stable)
#
# for ixx in range(2,21):
#     Table_printer(ixx)


# 5)
# with open ("2 Essa.txt", "r") as aa:
#     compress = aa.read()
#     compress=compress.replace("dashe" ,"#"*len("dashe") )
#
# with open ("2 Essa.txt", "w") as bb:
#     bb.write(compress)


# 6)
# with open("1 Essa.txt","r")as aa:
#      cont = aa.read()
#      if  "apple" in cont:
#          print("yes it have ")
#      else :
#          print("no")


# 7)
# def game_fun(ss):
#     with open("1 Essa.txt", 'r') as fil:
#         context=fil.read()
#
#     with open("1 Essa.txt", 'w') as filw:
#         if context=="":
#             context=0
#             filw.write(str(context))
#         if int(context) >= ss:
#            context=context
#            filw.write(context)
#         elif int(context) < ss:
#             context=ss
#             filw.write(str(context))
#
# for df in range(1,9):
#         aa=int (input("Enter a number: "))
#         game_fun(aa)



# ................................(    Project End     ).......................................














