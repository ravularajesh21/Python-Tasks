# List Comprehension
# Basically comprehensons are used to reduce the lines of code, we can do one operation of multiple lines of code in a single line of code.

# syntax = [expression for item in list if condition]

# I want to print the multipules of 3 using below list
L1 = [10,30,40,60,54,435,645,23,33,66,99,69]
div_by_3 = []

for num in L1:
    if num%3 == 0:
        div_by_3.append(num)
print("without using list comprehension",div_by_3)

# now trying same thing using list comprehension
print("using list comprehension",[num for num in L1 if num%3 == 0])
#Here when if condition satisfies then looping willbe done

#i want to do some operations using list comprehensions
print("values multiplied by 2 in range",[x**2 for x in range(1,8)])

print("squares of the vlaues in range",[x*x for x in range(7)])

print("cubes of values in range",[x**3 for x in range(12) if x%2==0])

# trying to print values and its wquares in n1 which are not repeated in n2
n1=[15,22,33,41]
n2=[33,42,50,65]
print("square of numbers which is not in n2 are ",[i**2 for i in n1 if i not in n2])

# splitting every word in string and printing capital letters of words and its length
words="the quick brown fox jumps over the lazy dog".split()
print(words)

print("capital letters of words and its length are",[[w.upper(),len(w)] for w in words])
















