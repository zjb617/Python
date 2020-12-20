import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
#上面一行等号后面返回一个名为Card的新元组子类，然后将类命名为等号前面的Card，所以一般第一个Card和第二个相同
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()#空参默认以空格分割

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
#单个下划线是一个Python命名约定，表示这个名称是供内部使用的。 它通常不由Python解释器强制执行，仅仅作为一种对程序员的提示

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')#创建beer_card对象
print(beer_card)

deck = FrenchDeck()
print(type(deck))
print(len(deck))

print(deck[0])
print(deck[-1])

#随机抽取一张牌
from random import choice
print(choice(deck))
print(choice(deck))
print(choice(deck))

print(deck[:3])
print(deck[12::13])#从12开始每隔13张拿一张牌

print('------------------------------------------------')

for card in deck:
    print(card)

for card in reversed(deck):
    print(card)


Card('Q', 'hearts') in deck#True
Card('7', 'beasts') in deck#False

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):#按照spades_high返回的值排序
    print(card)
print(sorted(deck, key=spades_high))
# key=lambda 元素: 元素[字段索引]
#上一行相当于下面三行
# def fun(元素):
# 	return 元素[字段索引]
# key = fun(元素)


