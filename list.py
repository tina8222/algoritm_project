 
#  List items are ordered, changeable, and allow duplicate values.
# mylist = ["apple", "orange", "cucumber","watermelon","orange"]
# print(len(mylist))   
# determine how many items a list has, use the len() function:

# newlist = list(("mew","meww","mew"))
# print(newlist)

# list can be contain of any type of data
# list2 = [1 , True, False,"apple", 6]
# print(list2)

# we can access to items with refering to index or neg index
# list3 = [1 , True, False,"apple", 6,99]
# print(list3[:-1])

# change item value

# list3 = [1 , True, False,"apple", 6,99]
# list3[1:4] = [False,True,"onion"]
# print(list3)

# list4 = [1,2,3]
# list4[1:2] = [4,5,6]
# print(list4)
# print(len(list4)) 

# list4 = [1,2,3]
# list4[1:3] = [4]
# print(list4)
# print(len(list4)) 

# insert methode
# 


# add items with 3 ways
# 1:append
# mylist = ["apple", "orange", "cucumber","watermelon","orange"]
# mylist.append("onion")
# print(mylist)


# 2:insert
# 3:extend you can combine list with set with this method
# mylist = ["apple", "orange", "cucumber","watermelon","orange"]
# my2list =(1,2,4.6)
# mylist.extend(my2list)
# print(mylist)

# 4 ways to remove or delete items
#1:remove
# mylist = ["apple", "orange", "cucumber","watermelon","orange"]
# mylist.remove("orange")
# print(mylist)


#2: .pop   If you do not specify the index, the pop() method removes the last item
# mylist = ["apple", "orange", "cucumber","watermelon","orange"]
# mylist.pop()
# print(mylist)

#3: del 
# mylist = ["apple", "orange", "cucumber","watermelon","orange"]
# del mylist[3]
# print(mylist)

# 4:clear
# mylist = ["apple", "orange", "cucumber","watermelon","orange"]
# mylist.clear()
# print(mylist)


# sort by alpha
# mylist = ["apple", "orange", "cucumber","Watermelon","orange"]
# mylist.sort(reverse=True)
# print(mylist)

# 3 ways tocopy list 
# .copy()
# list1 = [1,2,4,5]
# list2 = list1.copy()
# print(list2)

# list()
# list1 = [1,2,4,5]
# list3 =list(list1)
# print(list3)


# [:]
# listm = [4,5,6]
# mew = listm[:]
# print(mew)

# 2 way to join 2 list first operator + and second method extend
# list1 = [1,2,3,4]
# list2 = [9,8,7,6]
# list3 = list1 + list2
# print(list3)


# second way: extend.
# list1 = [1,2,3,4]
# list2 = [9,8,7,6]
# list1.extend(list2)
# print(list1)


# listn = [1,2,3,4]
# listb = [9,8,7,6]
# listn.append(listb)
# print(listn)
# listb khodesh y list joda mishvd


listy = [1,2,3,3,4,5,6,7,8,9,3]
x = listy.count(3)
print(x)












