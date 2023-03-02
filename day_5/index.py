# creating tuple
t1= 'a',
print(type(t1))

t = tuple('3')
# adding an item to an existing tuple
t+=('a','b')
print(t)
# tuples are imutable once declared 

# unpacking tuples 
x,y,w=(1,2,3)
print(x,y,w)

first,*more,last=(1,2,3,4,5)
print(first,*more,last)
