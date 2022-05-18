# Finding common items from two lists

x = [2,3,5,9,8,6,5]
y = [3,5,1,10,8,13,4]

z = set(x).intersection(set(y))
print(list(z))

# Replace the last element in a list with another list

li1 = [1, 3, 5, 7, 9, 10]
li2 = [2, 4, 6, 8]
newlist = li1[:-1] + li2
print(newlist)

# Extend a list without append

x = [10, 20, 30] 
y = [40, 50, 60]
x[:0] = y
print(x)

