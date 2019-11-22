import random

class Card:
    
    def __init__(self, rank, suit):
        '''
        Initializes a card object. Cards have a suit and rank. Asserts that the
        provided suit and rank are valid.

        Parameters:
          - rank (string): represents number 2-10, Jack, Queen, King, or Ace
          - suit (string): represents spade, heart, diamond, or club


        Returns: None
        ''' 
        
        #-----------------------------------------------------------------------------
        #1)  Checks for proper *rank*
        
        try:
            rank = int(rank) #first checks if user is trying to put 2-10
            
        except ValueError: #runs if it is not a number the user is trying to input
            assert rank in ['J','Q','K','A','T'], 'Error, must be the following: a number between 2-10 OR J, Q, K, or A '
        
        else:
            assert rank in range(2,11), 'Error, must be the following: a number between 2-10 OR J, Q, K, or A '
        
        #if an int, then checks the range
        
        
        rank = str(rank) #for the next .upper methods to work, must be ensured as a string
        
        #-----------------------------------------------------------------------------   
        
        #2)  Checks for proper *suit*
        
        assert suit in ['C','D','H','S'], 'Not a proper suit. Suits must be: C,D,H, or S'
        
        #-----------------------------------------------------------------------------
        self.__suit = suit.upper()
        self.__rank = rank.upper()        
    
        
    def isFaceCard(self):
        if self.__rank in ['J','Q','K']:
            return True
        return False
        
       
    def isAce(self):
        if self.__rank == 'A':
            return True
        return False
        
    def isNumeric(self):
        try:
            testNumeric = int(self.__rank)
        except ValueError:
            return False
        else:
            return True       

    def getRank(self):
        return self.__rank        
        
    def getSuit(self):
        return self.__suit        
        
    def __str__(self):
        '''
        Informal string representation of the Card object.
        
        Parameters: None
        
        Returns: string
        '''
        return self.__rank + self.__suit
        
        
class Deck:
    
    def __init__(self, capacity):
        assert type(capacity) == int, 'Critical Error: Capacity not int type!'
        assert capacity > 0, 'Error: negative capacity deck not possible irl...(u dummy fix ur file >:(  )'
        
        self.__deck = []
        self.__capacity = capacity
        self.__count = 0
        self.__tail = 0
        self.__head = 0
        

    def addCard(self, card):
        '''
        This function adds the input card to the bottom of the deck (queue)
        A circular Queue is implemented as adding a card to the tail of a queue
        is O(1) efficiency- the best efficiency.
        
        '''
        
        if self.__count == self.__capacity:
            raise Exception('Error: No cards to put back into Deck! Deck is full')
        if len(self.__deck) < self.__capacity:
            self.__deck.append(card)
        else:
            self.__deck[self.__tail] = card
        
        self.__count +=1
        self.__tail = (self.__tail +1) % self.__capacity
        
        #print(self.__deck)                
        
    def dealCard(self):
        
        '''
        This function removes the card from the top of the deck (queue)
        A circular Queue is implemented as returning a card from the head of a queue
        is O(1) efficiency- the best efficiency.
        
        '''        
        
        if self.__count == 0:
            raise Exception('Error: Deck is empty! All cards are being used')
        card = self.__deck[self.__head]
        self.__deck[self.__head] = None
        self.__count -= 1
        self.__head = (self.__head +1) % self.__capacity
        #print(self.__deck,'self.__deck in dealCard')
        return card
              

    def deckSize(self):
        return self.__count    
    
    def shuffle(self):
        random.shuffle(self.__deck)
        '''
        
        aux = []
        for i in self.__deck:
            if i != None:
                aux.append(i) #adds each card to the auxilary simple list
        auxLength = int(len(aux))
        print(auxLength)
        #following resets the deck as all the cards are in the aux and we do not want 
        #duplicate cards So 
        
        
        self.__count = 0
        self.__head = 0
        self.__tail = 0
        
        self.__deck = []
        
        while auxLength != 0: #uses addCard(random valid index) to refill the deck
            self.addCard(aux.pop(random.randint(0,auxLength-1)))
            auxLength -= 1  
        #print(self.__deck)
        '''
    def __str__(self): #invalid
        dash = ' - '
        newDeck = []
        for card in self.__deck:
            newDeck.append(str(card))
        return dash.join(newDeck)
        

if __name__ == '__main__':
    # test your Card class here
    
    Baccarat = Card('2','C')
    print(Baccarat.isFaceCard()) #checks 1st pos  
    print(Baccarat.isAce())      #checks 1st pos
    print(Baccarat.isNumeric())  #checks 1st pos
    print(Baccarat.getRank())    #returns 1st pos
    print(Baccarat.getSuit())    #returns 2nd pos
    
    #---Tests passed! :)
    
    
    # test your Deck class here
    
    deck = Deck(3)
    deck.addCard('ab')
    deck.addCard('bc')
    deck.addCard('cd')
    print(deck.dealCard())
    print(deck.dealCard())
    deck.addCard('eli')
    deck.addCard('cde')
        
    deck.shuffle()  
    print(deck.deckSize())
    
    
