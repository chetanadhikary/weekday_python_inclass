## Conditional Statements

##if <boolean expr>:
##    pythonstatements
##else:
##    python statements

## Program to find the greatest of three numbers
##x = 8
##y = 10
##z = 50

##if x>y and x>z:
##    print('X is the greatest integer')
##elif y>x and y>z:
##    print('Y is the greatest integer')
##else:
##    print('Z is the greatest integer')
##
##print('Program executed')
##

##Nested IF
##if x>y:
##    print('X is greater than Y')
##    if x>z:
##        print('X is greatest integer')
##    else:
##        print('Z is the greatest integer')    
##elif y>x:
##    if y>z:
##        print('Y is the greatest integer')
##    else:
##        print('Z is the greatest integer')
##    print('Y is greater than X')
##


# Write a program to check if a string is in
# title case. If not convert it to title case
##
##heading = input('Enter a Heading string')
##if heading.istitle():
##    print('Given string was in title format')
##else:
##    print('Not in title format')
##    print('Converted to ', heading.title())
##    #print(f'Converted to {heading.title()}')



# Write a program to check if a given string is a
# valid email ID
##Hint : check if '@' is present in the string
##
# email = input('Enter your email ID')

# if '@' in email:
#     print('Entered email Id is valid')
# else:
#     print('Please enter a valid email ID')


##Assignment :
##    Write a program to check if entered item by 
##    the user is a numerical datatype.
##    if numerical datatype:
##        perform addition
##    else:
##        perform concatenation


datatype1 = input('Enter the numerical data type1')
datatype2 = input('Enter the numerical data type2')

if (datatype1.isnumeric()):
    if (datatype2.isnumeric()):
        total=float(datatype1)+float(datatype2)
        print('Entered detials is datatype is',total)
    
  
else:
    print('Entered details is not numeric',datatype1+' '+datatype2)


## Write a program to prompt for a score between
##    0.0 and 1.0. If the
##score is out of range, print an error message. If
##    the score is between 0.0 and 1.0,
##print a grade using the following table:
##        Score Grade
##            >= 0.9 A
##            >= 0.8 B
##            >= 0.7 C
##            >= 0.6 D
##            < 0.6  F 
##
##
##grade = float(input('Enter a score between 0.0 and 1.0'))
##
##if grade > 1.0 or grade < 0.0 :
##    print('Error:Score is out of range')
##elif grade >= 0.9:
##    print('Grade obtained is A')
##elif grade >= 0.8 :
##    print('Grade obtained is B')
##elif grade >= 0.7:
##    print('Grade obtained is C')
##elif grade >= 0.6:
##    print('Grade obtained is D')
##else:
##    print('Grade obtained is F')


##grade = float(input('Enter a score between 0.0 and 1.0'))
##
##if grade < 1.0 and grade > 0.0 :    
##    if grade >= 0.9:
##        print('Grade obtained is A')
##    elif grade >= 0.8 :
##        print('Grade obtained is B')
##    elif grade >= 0.7:
##        print('Grade obtained is C')
##    elif grade >= 0.6:
##        print('Grade obtained is D')
##    else:
##        print('Grade obtained is F')
##else:
##    print('Error:Score is out of range')
