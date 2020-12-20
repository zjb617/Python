from nltk.book import *
from nltk import FreqDist
fdist = FreqDist(text6)
a = fdist.most_common(10)
b = fdist["Grail"]
print(a)
print(b)
