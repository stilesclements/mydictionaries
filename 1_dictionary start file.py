import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

'''

print()
print('*****  start section 1 - print dictionary ********')
print()


print(phonebook)
print(len(phonebook))
phone=phonebook['Chris']

print(phone)

phonebook={}

mydictionary=dict(m=8,n=9)
print(mydictionary)

print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()




name="chris"

if name in phonebook:
    phone=phonebook[name]
    print(phone)
else:
    print(f"{name} not found in phonebook")


print()
print('*****  end section 2 ********')
print()









print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook["Joe"]="555-0123"
phonebook["Chris"]="555-4444"
print(phonebook)

del phonebook["Chris"]

print(phonebook)

print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()




print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


for k in phonebook:
    print(f"the key is: {k} and the value is: {phonebook[k]}")

    for v in phonebook.values():
        print(v)
    
    for k,v in phonebook.items():
        print(f"the key is: {k} and the value is: {v}")



print()
print('*****  end section 5 ********')
print()




'''
print()
print('*****  start section 6 - using get and clear ********')
print()



phone=phonebook.get('katie','911')
print(phone)

phonebook.clear()

print(phonebook)

'''
print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

print(phonebook)
phone=phonebook.pop('Katie','911')
print(phone)
print(phonebook)



print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

print(phonebook)
phone=phonebook.popitem()
print(phone)
print(phonebook)



print()
print('*****  end section 8 ********')
print()

'''
'''
print()
print('*****  start section 9 - using random and converting to list ********')
print()


print(phonebook[random.choice(list(phonebook))])

print()
print('*****  end section 9 ********')
print()


'''
