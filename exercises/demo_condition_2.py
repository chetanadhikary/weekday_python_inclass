# Conditional Statements with lists

#lst_num = [1,2,3,4,5]
dict_num = {1:1,2:4,3:9,4:16}

##
##num1 = float(input('Enter a number'))
##
##if num1 in lst_num:
##    print('Number is in the list')
##else:
##    print('Entered number is not in the list')
##

##
##num1 = float(input('Enter a number'))
##
##if num1 in dict_num.values():
##    print('Number is in the keys list')
##else:
##    print('Entered number is not in the  keys list')
##
##

# Program to find the pair of square
# (1,1),(2,4)

#num1 = float(input('Enter a number pair'))
##num1 ,num2 = (1,1)
##
##if (num1 in dict_num.keys()) and (num2 in dict_num.values()):
##    print('Number pair is in the dictionary')
##else:
##    print('Entered number is not in the  dictionary')
##

##
##num1 ,num2 = (2,8)
##
##if (num1,num2) in dict_num.items():
##    print('Number pair is in the dictionary')
##else:
##    print('Entered number pair is not in the  dictionary')


##
##num1 = [1,2,3,4,5]
##num2 = [6,7,8,9]
##num3 = [10,11,12,13]
##tup_num = ((1,6,10),(2,7,11),(3,8,12))
##
##if (num1[0],num2[0],num3[0]) in tup_num:
##    print('Numbers found')
##else:
##    print('Numbers not found')

# Program to check if a student belongs to a class
##dict_class = {'A':['Harry','Ron','Harmoine'],'B':['Aishwarya','Chaitra','Nithin'],
##              'C':['chetan','Vikram','Harshavardhan']}
##
##name = input('Enter the student name:')
##
##if name in dict_class['A'] :
##    print(f'{name} is in class A')
##elif name in dict_class['B'] :
##    print(f'{name} in class B')
##elif name in dict_class['C']:
##    print(f'{name} is in class C')



# Program to check if a patient can consume a fruit
# consumable_fruits = ['apple','jackfruit','mango','raspberry']
# non-consumable fruits = ['banana','orange','watermelon','musk melon']
# If not there in the list , prompt patient to consult the doctor
fruit = input('Enter a fruit to check')
####Using Lists
##lst_consumable_fruits = ['apple','jackfruit','mango','raspberry']
##lst_non_consumable_fruits = ['banana','orange','watermelon','musk melon']
##
##
##if fruit in lst_consumable_fruits:
##    print('You can have this fruit')
##elif fruit in lst_non_consumable_fruits:
##    print('You are forbidden to consume this fruit')
##else:
##    print(f'I am not sure of the fruit {fruit}\nPlease consult your doctor')
##    
##

####Using Dictionary
dict_fruits = {'consumable':['apple','jackfruit','mango','raspberry'],
               'non_consumable':['banana','orange','watermelon','musk melon']
               }

if fruit in dict_fruits['consumable']:
    print('You can have this fruit')
elif fruit in dict_fruits['non_consumable']:
    print('You are forbidden to consume this fruit')
else:
##    dict_fruits['unknown'].append(fruit)
##    dict_fruits['unknown'] = dict_fruits.get('unknown',fruit)
    if 'unknown' in dict_fruits.keys():
        print(dict_fruits['unknown'])
    else:
        dict_fruits['unknown'] = fruit
    print(f'I am not sure of the fruit {fruit}\nPlease consult your doctor')
    print(dict_fruits)





















