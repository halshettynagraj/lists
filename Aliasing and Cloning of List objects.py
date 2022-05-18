from tkinter import Y


x = [10,12,30,40]
y = [10,12,30,40]
print (x == y) 
print(x is y)
y = x 
print(x==y)


# copy()

p = ["Python is fun"]
q = p.copy()
print(q)