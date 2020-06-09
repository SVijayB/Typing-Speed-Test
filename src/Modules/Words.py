import urllib.request
import random
import time

def words(choice):
    data = open("assets\dictionary.txt","r").read()
    words = data.splitlines()
    basic_words = []
    j = 3
    if(choice == 1):
        i = 20
    elif(choice == 2):
        i = 7
    elif(choice == 3):
        i = 12; j = 5
    for x in words:
        if(len(x) < i and len(x) > j):
            basic_words.append(x)
    randwords = random.sample(basic_words,200)
    result = ""
    for x in randwords:
        result = x + "\n" +result
    return result

print(words(2))