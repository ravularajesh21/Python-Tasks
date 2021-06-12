# Math operation

num1=int(input('enter first number:'))
num2=int(input('enter second number:'))

option=int(input('enter option:'))
if option==1:
    print('Addition is',num1+num2)
elif option==2:
    print('Substraction is',num1-num2)
elif option==3:
    print('Multiplication is',num1*num2)
elif option==4:
    print('Division is',num1/num2)
elif option==5:
    print('Floor Division is',num1//num2)
else:
    print('Invalid option try again')