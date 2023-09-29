#The program should create a dictionary in which the keys 
#are the individual words found in the file and the values 
#are the number of times each word appears. For example, if the word “the” 
#appears 128 times, the dictionary would contain an element with 'the' as the 
#key and 128 as the value. The program should display the frequency of each word.


from pyparsing import Word


infile=open("sometext.txt",'r')
Word_dict={}

#Create word list
for line in infile:
    wordlist=line.split()

#Clean list
for wordnum in range(len(wordlist)):
    word=wordlist[wordnum]
    word=word.rstrip(",")
    word=word.rstrip(".")
    word=word.lower()
    wordlist[wordnum]=word

#Count words and add to dict
for word in wordlist:
    if word in Word_dict:
        Word_dict[word]=Word_dict[word]+1
    else:
        Word_dict[word]=1

#Print dict
for word in Word_dict:
    print(word,": ",Word_dict[word],sep="")
infile.close()