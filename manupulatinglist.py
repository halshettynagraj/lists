# manupulating elements of list

# append()

x = [25, 2.3, "python", "asdfjkl;", 95, 58]

x.append("Django")
print(x)

#insert()

x.insert(2,100)
print(x)

# Differences between append() and insert()

# append() method will be add a new element to list in the end of given list.
# insert() method will be add a new element to list with given index number. we have to  2 arguments with insert method.


# Extend()
y = [21,66,85,96,2.32,"nagraj"]
z = ["python", 3.8]

y.extend(z)
print(y)
print(z)

# extend() method will concatanate the values from 2 lists (As you seen in an above program ) 

# remove()

p = [13,56,32,56,66,67,66,63,66]

p.remove(66)
print(p)

# pop()

p.pop(2)
print(p)

# remove() method removes the perticular value which is given. 
# pop() method removes the last element of list. also it will remove the index value of element.