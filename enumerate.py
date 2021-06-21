#  ENUMERATE()

# if we need only one element enumerate
str1= ['Hello','python',True,'False','rajesh','easy']
e=enumerate(str1)
count,value=e.__next__()
print(count,value)


# if we want all the elements enumerate

str1= ['Hello','python',True,'False','rajesh','easy']
enum = enumerate(str1)

print(tuple(enumerate(str1,2)))