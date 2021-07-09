

t1 = (10)
print(t1)
print(type(t1))

t2 = ('Python')
print(t2)
print(type(t2))

t1 = (10,)
print(t1)
print(type(t1))

t2 = ('Python',)
print(t2)
print(type(t2))


t1 = (10,20,'rajesh',2.5,10+25j)
print(t1)
print(type(t1))

t2 = tuple(range(10,110,10))              # to get the output in tuple
print(type(t2))
print(t2)

t3 = tuple([10,20,30,40,50])
print(t3)
print(type(t3))

t3 = ([10,20,30,40,50])                   # to get the output in list format
print(t3)
print(type(t3))

t4 = tuple('python')
print(t4)
print(type(t4))

t5 = tuple((10,20,30,40,50))
print(t5)
print(type(t5))

#t6 = tuple(10)
#print(t6)


# Indexing

tuple1 = (10, 20, 30, 1.5, 3.3, True, 'Python',3+6j)
print(tuple1[0])
print(tuple1[4])
print(tuple1[6])
print(tuple1[-1])

# Slicing

tuple1 = (10, 20, 30, 1.5, 3.3, True,'Mahathi','Python',3+6j,45,False)
print(tuple1[:3])
print(tuple1[3:])
print(tuple1[::2])

# Immutable
tuple2 = (11,22,35,44,55)
tuple2[0]=10
print(tuple2)


tuple2.pop()
print(tuple2)

#  convert from tuple to list

list1 = list((10,20,30))
list1.append(True)
list1.append('ATM')
list1.append(2+5j)
print(list1)
print(type(list1))

# convert from list to tuple

t1 = tuple(list1)
print(t1)
print(type(t1))













