# list
# a = [1,2,3,4]
# print(len(a)-1)

# list inside list
# data = [1,2,3,4,["Nishan","rana"],4]
# print(len(data))
# print(data[4][1])

# slicing
# items =["apple","banana","cherry","date","fig","grape","kiwi","lemon","mango","orange"]
# print(items[2:6])
# print(items[:5])

# list method for add
# - append
# - insert
# - concat

# append -- add data in list at last
# a = [1,2]
# a.append([3,9])
# a.append(4)
# a.append(5)
# a.append(6)
# print(a)

# insert -- add data at any place but index must be given
# a =["suman","sharma","virat"]
# a.insert(1,"kumar")
# a.insert(3,"hello")
# a.insert(4,"world")
# print(a)

# extend -- add two list
# a =[1,2,3,4,5]
# b =[6,7,8]
# a.extend(b)
# b.extend(a)
# print(a)
# print(b)

# concat 
# a =[1,2,3,4,5]
# b =[6,7,8]
# print(a+b)
# de
# a =[1,2,3,4,[5],[6,[[[7,[[8]]]]]],[[9]]]
# def list1 (lst):
#     flat = []
#     for item in lst:
#         if type(item) == list:
#             flat += list1(item)  
#         else:
#             flat.append(item)
#     return flat

# a = [1, 2, 3, 4, [5], [6, [[[7, [[8]]]]]], [[9]]]

# print(list1(a))

# remove
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# pop
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# del
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# clear
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# sort
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# sort in reverse decending order
# a =[1,2,3,4,5]
# a.sort(reverse=True)
# print(a)

# reverse form back
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# find second largest number in a list
# a = [4, 2, 7, 8, 9, 3]
# a.sort()
# print(a)           
# print(a[-2])       

# Given a list with possible duplicates, return a list 
# containing the last 3 unique elements keeping their original order.
# a = [1,2,3,2,4,5,3,6,5,7]
# print(a[7:])

# remove duplicate data
# my_list = [1, 2, 3, 2, 4, 5, 1]
# print(my_list)
# unique_list = list(set(my_list))
# print(unique_list)


# Write Python code to:
# --Retrieve the third element of the list.
# --Create a new list that contains only the first three elements.
# --Replace the last element of the list with 100.
# --Check if the number 40 is in the list.
# --Find the length of the list.

# num = [10,20,30,40,50,60]
# print(num[2])
# print(num[:3])
# num[-1]=100
# print(num)
# print(40 in num)
# print(len(num))




