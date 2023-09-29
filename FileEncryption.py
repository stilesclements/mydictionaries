import string
import random
infile=open("info_security.txt",'r')

codes_dict={}
#extract text from the file as a string
for line in infile:
    text=line

#Make a list of a letters, digits, and symbols to use for encryption
character_list=[]
for letter in (string.ascii_letters+string.digits+string.punctuation):
    character_list.append(letter)


outfile=open("encrypted.txt",'w')

#For each letter check to see if in dict, and if not, add it and assign an encrypted character using random draw from the list character_list
#Then write the character and its assigned encrypted character to the dictionary. 
for letter in text:
    if letter not in codes_dict:
        random_char=character_list.pop(random.choice(range(len(character_list))))
        codes_dict[letter]=random_char
    outfile.write(codes_dict[letter])
print(codes_dict)

infile.close()
outfile.close()









        




