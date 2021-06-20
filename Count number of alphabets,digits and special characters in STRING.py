#  Count number of alphabets,digits and special characters


string=input('enter string:')
alphabetcount=0 
digitcount=0 
specialcharactercount = 0
for x in string:
    if x>='A' and x<='Z' or x>='a' and x<='z':
        alphabetcount = alphabetcount + 1
    elif x>='0' and x<='9':
        digitcount=digitcount + 1
    else:
        specialcharactercount = specialcharactercount+1
print('Alphabet count',alphabetcount)
print('digit count',digitcount)
print('special character count',specialcharactercount)
        