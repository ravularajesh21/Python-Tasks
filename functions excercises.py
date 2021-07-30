# Write a Python function to sum all the numbers in a list.

number = [14,15,26,30,71,84,63]
def num(number):
    total = 0
    for j in number:
        total =total+j
    print(total)
print(sum(number))


# Write a Python function to multiply all the numbers in a list.

number = [4,8,2]
def num(number):
    total = 1
    for j in number:
        total =total*j
    print(total)
print(multiply(number))


# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
str1 = input('enter strings:')
def string(str1):
    d={'UPPER_CASE':0,"LOWER_CASE":0}
    for x in str1:
        if x.isupper():
            d["UPPER_CASE"]+=1
        elif x.islower():
            d['LOWER_CASE']+=1
        else:
            pass
    print('Original Characters',str1)
    print('No of characters Upper case',d["UPPER_CASE"])
    print('No of characters Lower case',d['LOWER_CASE'])
string(str1)


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unque(list1):
    x = []
    for i in list1:
        if i not in x:
            x.append(i)
    print(x)
unque([1,2,3,4,5])

# Write a Python program to access a function inside a function.

def test(a):
        def add(b):
                nonlocal a
                a += 1
                return a+b
        return add
func= test(4)
print(func(4))