# Write a Python program that accepts an integer (n) 
#   and computes the value of n+nn+nnn. 
# Sample value of n is 5             5+55+555=615
# Expected Result : 615



b=int(input('enter number:'))
a1=int('%a' %b)
a2=int('%a%a' %(b,b))
a3=int('%s%a%a' %(b,b,b))
print(a1+a2+a3)

