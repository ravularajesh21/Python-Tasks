# Following the square series

number=int(input('enter number:'))
for value in range(1,number+1):
    print(value**2,end=(' '))
print()

# Following the series 1**1,2**2,3**3

num=int(input('enter number:'))
for data in range(1,num+1):
    print(data**data,end=(' '))
    
# Following the series   10 20 30 40 50 60

num=int(input('enter number:'))
for i in range(1,num+1):
    print(i*10,end=(' '))
    
    
# Generate the sum of the following series     1+2+3+4+5+6 =  21
#sum of n numbers

number=int(input('enter value'))
sum=0
for j in range(1,number+1):
    sum=sum+j
print('sum of series:',sum)

# sum of n numbers in input n number from keyboard and find sum

n=int(input('enter number:'))
sum=0
for x in range(n):
    num=int(input('enter number:'))
    sum=sum+num
print('The sum of',n,'number is',sum)



















    