import urllib.request
import random
import time

def words():
    url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib.request.urlopen(url)
    data = str(response.read().decode())
    words = data.splitlines()
    basic_words = []
    for x in words:
        if(len(x) < 7 and len(x)>3):
            basic_words.append(x)
    randwords = random.sample(basic_words,200)
    result = ""
    for x in randwords:
        result = x + "\n" +result
    return result

print(words())