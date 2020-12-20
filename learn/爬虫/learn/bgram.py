from nltk.book import text6
from nltk import bigrams, FreqDist
bigrams = bigrams(text6)
bigramsDist = FreqDist(bigrams)
print(bigramsDist[("Sir", "Robin")])
