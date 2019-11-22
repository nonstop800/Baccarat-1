from playing_cards import Card, Deck
from baccarat import Player, Table


table = Table()
table.populateDeck()
table.displayTable() #shows empty table with a full deck
table.deal(0)
table.deal(1)
table.deal(2)
table.deal(3)
table.deal(4)
table.deal(5)
table.deal(6)
table.deal(7)
table.deal(8)

table.displayTable()
print(table.checkTableValues(), 'tableValues()', type(table.checkTableValues()))
print(table.cardsRemaining())

table.clearTable()
table.displayTable()
table.newDeck()
table.displayTable()

#?????????



'''
baccarat = Player()
card = Card('9', 'H')

baccarat.updateHand(card)
card = Card('A', 'S')
baccarat.updateHand(card)
card = Card('K', 'H')
baccarat.updateHand(card)

print(baccarat.getHandValue())

print(baccarat.getHand()) #INVALID:PRINTS THE OBJECT. MUST CHANGE

table = Table()
table.populateDeck()
print(table.cardsRemaining())

table.displayTable()#INVALID: PRINTS THE OBJECT... MUST CHANGE
table.deal(1)
table.displayTable()
table.deal(2)
table.displayTable()
table.clearTable()
table.deal(1)
table.deal(2)
table.deal(3)
table.deal(4)
table.displayTable()
table.checkTableValues()

table.newDeck()
table.displayTable()
table.deal(0)
table.deal(1)
table.displayTable()
print(table.cardsRemaining())
'''
