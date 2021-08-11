# Dictionary Comprehension

#using dict comprehension printing some math operations
print("squares of numbers in the form of dict",{x:x*x for x in range(2,9)})

print("dictionary is multiplied by 2 are", {x:x*2 for x in range(1,7)})

#trying to add both values of a in one key
dict = {'a':35, "b":76, "A":15}
print({k.lower():dict.get(k.lower(), 0)+dict.get(k.upper(), 0) for k in dict.keys()})

#here both vlaues of a and A ==> 35+15 is added into a


# Set Comprehensions

# in sets, o/p will not come in sequence, it will print all values randomly
print("squares of the numbers ",{x*x for x in range(8)})

print("multiplying the set with 5 ",{x*5 for x in {1,2,3,4,4,5,5,6,6,7,7,8}})
#even though we given duplicate values in set, it wont take duplicates in set

#set object doesn't support indexing