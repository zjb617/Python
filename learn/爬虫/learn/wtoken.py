from nltk.book import *
from nltk import word_tokenize
text = word_tokenize("Strange women lying in ponds distributing swords is no basis for a system of government. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony.")
from nltk import pos_tag
print(pos_tag(text))#结果参考Penny Treebank标记表