
aa=12
bb=12.33
cc="Agha Essa khan"
dd=12+2j
ee=True

print(f"Integer data type value ( {aa} ) and It's Type is  ( {type(aa)} )\n")
print(f"Float data type value ( {bb} ) and It's Type is  ( {type(bb)} )\n")
print(f"String data type value ( {cc} ) and It's Type is  ( {type(cc)} )\n")
print(f"complex data type value ( {dd} ) and It's Type is  ( {type(dd)} )\n")
print(f"boolean data type value ( {ee}  )and It's Type  is ( {type(ee)} )\n")





favourite_colors=["red","blue","green","voilet"]
print (f"the First color is :{favourite_colors[0]}\n")
print (f"the Last color is :{favourite_colors[-1]}\n")
favourite_colors.append("GreyBlack")
print(f"All colors : {" , ".join(map(str,favourite_colors))}\n")




Essa_set_uni={22,44,88,67,90,110,120}
Essa_set_uni.add(145)
Essa_set_uni.remove(44)
print(f"all set values are :{Essa_set_uni}")



favourit_fruit_tuple=("apple","orange","pinaple","cherry")
print(f"second fruit name from my tuple :{favourit_fruit_tuple[1]}\n")
print (f"the length of tuple:{len(favourit_fruit_tuple)}\n")

favourit_fruit_tuple[0]="banana"  #tuple is immutable so that’s why it’s values can’t be changeable and show error






Student_dict={
    "Ali":12,
    "Agha Essa":13,
    "Mustfa":52,
    "Ahmad":42

}
print(f"the age of Agha Essa is :{Student_dict['Agha Essa']}\n")
Student_dict["Zeshan"]=99   #add new student
print(Student_dict)







even_set={2,22,44,88,66,6}
check=88
print (f"the number {check} is present in my set? :{check in even_set}\n"  )
print (f"the number {50} is present in my set? :{50 in even_set}\n"  )
















dict={
    "biscuits":100,
    "lemon":94,
    "cooking port":820,
    "pencil":26
}
print(f"the lemon price is {dict["lemon"]} Rs. only\n")







Essa="""Hello! My name is Agha Essa Khan.
I am 20 years old and I live in Lahore.
My hobbies include Watching Anime series and coding.
My favorite subject is Computer Science.
I love pizza as my favorite food.
My favorite programming language is Python.
My dream job is to be a software engineer.
A fun fact about me is that I chose to learn Python in my second semester, while most of my \npeers were focused on chasing their GPAs. I believe in the power of skills over scores.
Thank you for listening!"""
print(Essa)