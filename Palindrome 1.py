# Approach 1

date = input('enter the date in dd/mm/yyyy format:')
given_date = date.replace('/', '')
reversed_date = given_date[::-1]
if given_date == reversed_date:
    print(date,'is palindrome')
else:
    print('It is not palindrome')
    
    
# Approach 2 

day = input('enter day:')
month = input('enter month:')
year = input('enter year:')

given_date = day+month+year
reversed_date = given_date[::-1]
if given_date == reversed_date:
    print('date is not palindrome')
else:
    print('date is not palindrome')
    
    