# print ("lets started")
# print ("..............................................................................")
# ................................( Project Number : 1 ).......................................
# import pyjokes
# # joke num1
# print ("printing jokes....")
# joke =pyjokes.get_joke()
# print (joke)
# ................................(    Project End     ).......................................
#
# # comment......
# '''hsjsjs
# sjjk
# schjxhsks
# jxsjx
# '''
# print ("..............................................................................")
# # poem comment ......
# print (''' an arrangement of words written or spoken:
# traditionally a rhythmical composition, sometimes rhymed,
# expressing experiences, ideas, or emotions in a style more
# concentrated, imaginative, and powerful than that of ordinary
# speech or prose: some poems are in meter, some in free verse.
# POEM definition and meaning | Collins English Dictionary
# Collins Dictionary ''' )
# print ("..............................................................................")
#
# ................................( Project Number : 2 ).......................................

"""
import pyttsx3
engine = pyttsx3.init()
engine.say('''Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!
Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are''')
engine.runAndWait()
"""


# ................................(    Project End     ).......................................

# ................................( Project Number : 3 ).......................................
# print ("..............................................................................")
# # directory of our computer printing ................
# import os
# # Specify the directory you want to list
# # koi sa bhi document kholwa loo bus "/" sath likhna he...ok or name complete full
# directory = "/third semester.......(3)"
# try:
# # Get the list of all files and directories in the specified directory
#     contents = os.listdir(directory)
#     print(f"Contents of '{directory}':")
#     print(contents)
# except FileNotFoundError:
#     print(f"The directory '{directory}' does not exist.")
# except PermissionError:
#     print(f"Permission denied to access '{directory}'.")
#
# ................................(    Project End     ).......................................
#
#
# # or operator used ...
# print ("The true or false is : ",True or  False)
# print ("The false or false is : ",False or  False)
#
#
# # and operator used ...
# print ("The true and false is : ",True and  False)
# print ("The false and false is : ",False and  False)
# print ("..............................................................................")
#
# # not operator used ......
# print ("When not(!) operator used in True values :", not (True))
# print ("When not(!) operator used in False values :", not (False))
# print ("..............................................................................")
# bb= True
# print (not (bb))



# ................................( Project Number : 4 ).......................................

""""
# ...........................(Type Casting and conversions).............................................
# ........................................
num1=22
# show=type(num1)
# print (show)
#           or
print (type(num1))
# .......................................

n1=22          #int convert to string type
dot1=str(n1)
print (type(dot1))

# .......................................

ff="33"
gf=int (ff)
print (type(gf))

# .......................................

"""
# ................................(    Project End     ).......................................


#......................($$$ (Short Cuts ofs... ) $$$ ).......................

# 1 )
# finding the type of any variable
# rr=22.3            # Ctrl+shift+p
# ggd=2              # Ctrl+shift+p
# ffks="uwuwh"       # Ctrl+shift+p
# dsshsj=9999999999999999999999999999999999999999999999999   # Ctrl+shift+p

# ............................................................................

# 2 )
# Duplicate the line or any thing
# aaa="""hssjjjsjssjjs"""
# aaa="""hssjjjsjssjjs"""    #..............(Ctrl+D)
# aaa="""hssjjjsjssjjs"""
# aaa="""hssjjjsjssjjs"""

# ............................................................................

# ................................( Project Number : 4 ).......................................

# val1=int  ( input ("Enter number 1 : "))
# val2=int  ( input ("Enter number 2 : "))
# print (val1+val2)
#
# # or
#
# val1=int  ( input ("Enter number 1 : "))
# val2=int  ( input ("Enter number 2 : "))+val1
# print (val2)

# ................................(    Project End     ).......................................

# a=input ("Enter any thing to show its type  : ")
# print (type(a))

# b=int (input ("enter num 1 : "))
# d=int (input ("enter num 2 : "))
# print ("Average of these nums : ", (b+d)/2)



# bs=int (input ("enter num  : "))
# print ("Square of this num : ", bs**2)

# ............................................................................................

# ................................( Project Number : 5 ).......................................

# name ="Agha_Essa_khan"
# print ("Given : ",name)
# print ("Length of name is : ", len(name))  # finding length of name
# ff=int (input ("Enter Start  length Number : "))
# vv=int (input ("Enter  end   length Number : "))
# print (name[ff:vv])


# ................................(    Project End     ).......................................





"""
# .....................................(strings all)..................................





# v11="Aghaessawj ww"
# print (v11[0:10:3])
# 
# b2="gsjsxuwn3iisjs.dn"
# print ("length : ",len(b2))
# 
# print (b2[1:17:4])
# suis








# ............................string function.........................
# na1="aghaEssa"
# print (na1.endswith("ssa"))
#
# print (na1.endswith("a"))
# print (na1.startswith("AgH"))
# print (na1.capitalize())





# num5="agha is a good and good and good and  the a boy"
# print (num5.replace('good','bad'))              # Replacings..............
# print (num5.replace("a","yyx"))




# 
# fkf="                    What Do you mean BYYY"
# print(fkf.lower())
# print (fkf.upper())
# print (fkf.capitalize())
# print (fkf.title())
# print (fkf.lstrip()) #remove leading gap in  string




# 
# ddd="how are you by the way ..."  # splitting the string into list.............
# print (ddd.split())
# print (ddd.find("are"))   # find some thing with it .....ok



"""

# .......................................................................................





# ................................(Escape sequences and methods).....................

# line ="How I\twonder \nwhat you\tare and what you\tare \nbut forget 'about' that\n you know \"what\"........"
# print (line)


# ......................................................................................



# ................................( Project Number : 7 ).......................................

# 1) (fstring) usage in in out used important
# fga="Essa"
# sent= input ("Enter Your name : ")
# print (f"Welcome to the industry  {sent} I Admire you {fga}")
#
# 2)
# #  replacing in the long string by chain replace.............***************
# longstring='''
#       he has to achieve his goals
#       but seams utterly unconscious
#       at the way of light......#
# '''
# print (longstring.replace("achieve","claim").replace("unconscious","ghted").replace("light","Emerging_majestic"))


# # 3)
# sentence = "Hi,\n\tWhat you are doing right now...!\nBy the way"
# print (sentence)
#
#
# # 4) find word index
# print (sentence.find("What"))
#
#
# # 5) replacement in sentence.......
# print (sentence.replace("are","is"))
#

# ................................(    Project End     ).......................................




                                       # LISTS
# Lists are mutable (can be changed but strings can not changed once they are written imuttable)
# lists and their methods...........

# store=["apple","dash","ghk",2222,22.78,'Q',"222","straw"]
# print (store)
# print (store[0])
# print (store[5])
# store[1]="3jks"
# store[2]="wess",99
# print (store)

# append method in lists...............(1)
# store.append("essa1")
# print (store)
# store.append("essa2")
# print (store)

# sort method in lists.................(2)
# array=[4,5,77,92,6,0,22,84,222,782317]
# array.sort()
# print (array)

# reverse method in lists..............(3)
# array.reverse()
# print (array)

# pop method in lists..................(4)
# remove value from list and return that value  which he remove from the list
# print (array.pop(3))
# print (array)

# insert method in lists..................(5)
# darray=["cast",2,33,"sd",'d']
# print(darray)
# darray.insert(2,"yaloooo")
# print (darray)
# # ................................................................................
# darray.insert(2,"next")
# print (darray)
# darray.pop(3)
# print (darray)
#
# # remove method in lists......................(6)
# darray.remove(33)
# print (darray)
# # ................................................
# darray.remove("next")
# print (darray)



# **************************************************************************************











































