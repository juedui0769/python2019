# 流畅的Python
# 第1章 Python数据模型

# 示例1-1 一摞有序的纸牌

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

class ChinaPoker:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = '方片 黑桃 梅花 红桃'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

def poker():
    _poker = ChinaPoker()
    suit_values = dict(红桃=3, 梅花=2, 黑桃=1, 方片=0)
    def spades_high(_card):
        rank_value = ChinaPoker.ranks.index(_card.rank)
        return rank_value * len(suit_values) + suit_values[_card.suit]
    for _card in sorted(_poker, key=spades_high):
        print(_card)

def deck():
    _deck = FrenchDeck()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    def spades_high(_card):
        rank_value = FrenchDeck.ranks.index(_card.rank)
        return rank_value * len(suit_values) + suit_values[_card.suit]
    for _card in sorted(_deck, key=spades_high):
        print(_card)

if __name__ == '__main__':
    deck()
    print('='*20)
    poker()
    print('=' * 20)
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    poker = ChinaPoker()
    print(len(poker))
    print(poker[0])
    print(poker[-1])
    print('-'*20)
    for card in poker:
        print(card)
    print("*"*20)
    def hello():
        print('hello world')
    hello()


