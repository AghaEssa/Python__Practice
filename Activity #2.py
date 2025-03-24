my_list = [10, 20, 30, 40, 50, 60, 70]
print(my_list[2:5])


last_three_elements= my_list[4:]
print(last_three_elements)


print(f"Reverse list :{my_list[::-1]}")


text ="Laila, Zahra"
print(text[7:])



fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(fruits)


list_numbers=[]
list_numbers.insert(0,10)
list_numbers.insert(1,20)
list_numbers.insert(2,30)
print(list_numbers)




list_info = ["Laila", "Zahra", "Lecturer"]
list_info.insert(0,"SST")
print(list_info)


list_fruits = ["apple", "banana", "cherry"]
list_fruits.insert(1,"orange")
print(list_fruits)


list_colors = ["red", "blue", "green"]
list_colors.insert(0, "yellow")
print(list_colors)


list_mixed= [1, "two", 3.0, "four", 5]
print(list_mixed)
new_list_mixed = list_mixed[1:4]
print(f"middle three elements: {new_list_mixed}")
new_list_mixed.insert(2,"new")
print (new_list_mixed)
list_mixed[0]=str(list_mixed[0])
list_mixed[2]=str(list_mixed[2])
list_mixed[4]=str(list_mixed[4])
print(f"After convertion in to string : {list_mixed}")
