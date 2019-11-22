from playing_cards import Card, Deck

class Player:
    def __init__(self):
        self.__hand = [] #order does not matter
        self.__handValue = 0
    
    def updateHand(self, card):
              
        #Adds card to the player's hand. Point value is updated accordingly
        self.__hand.append(card)
                   
        
        if card.getRank() == 'A':
            self.__handValue += 1
        elif card.getRank() == '2':
            self.__handValue += 2
        elif card.getRank() == '3':
            self.__handValue += 3
        elif card.getRank() == '4':
            self.__handValue += 4
        elif card.getRank() == '5':
            self.__handValue += 5
        elif card.getRank() == '6':
            self.__handValue += 6
        elif card.getRank() == '7':
            self.__handValue += 7
        elif card.getRank() == '8':
            self.__handValue += 8            
        elif card.getRank() == '9':
            self.__handValue += 9   
        elif card.getRank() == 'T' or card.getRank() == 'J' or card.getRank() == 'Q' or card.getRank() == 'K':
            pass
            
    def clearHand(self):
        #clears the hand and resets the value to 0
        self.__hand = []
        self.__handValue = 0
        
    
    def getHand(self):
        #returns the current hand
        return self.__hand
        
    
    def getHandValue(self):
        #returns the current hand value
        return self.__handValue
        
                
    
class Table:
    def __init__(self):
        self.__deck = Deck(52)
        #there are two players, therefore, 2 player instances are called!
        self.__playerHand = Player()
        self.__dealerHand = Player()
        self.__discardPile = []
        
    
    def populateDeck(self):
        fileFound = False
        while not fileFound:
            try: 
                user = input('Please put deck file name: ')
                file = open(user, "r")
                
            except FileNotFoundError:
                print('Invalid file, please try again') 
            else:
                fileFound = True
                checkList = []
                for line in file:
                    checkList.append(line) #to check whether there are duplicates and/or deck size is valid
                    List = []
                    for i in line:
                        List.append(i)
                    
                    self.__deck.addCard(Card(List[0],List[1])) #what should I add as the object
                    
                
                
                if len(set(checkList)) != len(list(checkList)): #set to list comparision
                    raise Exception('There are duplicates in this deck!')
                
                elif len(checkList) != 52:                   
                    raise Exception('Not a proper deck size!', len(checkList))
                        
                   
    def cardsRemaining(self):
        return self.__deck.deckSize()
            
    def deal(self, toWho):
        if toWho % 2 == 1:
            card = self.__deck.dealCard()
            self.__dealerHand.updateHand(card)
            return card 
                        
        else:
            card = self.__deck.dealCard()
            self.__playerHand.updateHand(card)
            return card
              
    
    def displayTable(self):
        '''
        print('---------------------')
        print('Deck: ',self.__deck)
        '''
        player_hand = ' '
        dealer_hand = ' '
        #!!!!!!!why does this print as an object and not the str rep??
        print('Player hand: ', player_hand.join([str(i) for i in self.__playerHand.getHand()]), ' ---> ', 'Score =' , self.__playerHand.getHandValue())
        print('Dealer hand: ', dealer_hand.join([str(i) for i in self.__dealerHand.getHand()]), ' ---> ', 'Score =' , self.__dealerHand.getHandValue())
        #print('discard Pile: ', self.__discardPile)
        #print('discard pile: ', [str(i) for i in self.__discardPile])
    
    def checkTableValues(self):
        '''
        print(self.__playerHand.getHandValue())
        print(self.__dealerHand.getHandValue())
        '''
        
        playervalue  = self.__playerHand.getHandValue()
        dealervalue = self.__dealerHand.getHandValue()
        #return a tuple of (playerHand value, dealerHand value)
        return (self.__playerHand.getHandValue(), self.__dealerHand.getHandValue())
         
        
        
    
    def clearTable(self):
        '''
        This action will remove all current cards on the table in both hands and places them in the discard pile. Deck is untouched.
        
        NOTE: CALL THIS FUNCTION BEFORE CALLING newDeck()
        
        '''
        
        for playercard in self.__playerHand.getHand():
            
            self.__discardPile.append(playercard) 
        
        for dealercard in self.__dealerHand.getHand():   
            self.__discardPile.append(dealercard)
        
        self.__playerHand.clearHand()
        self.__dealerHand.clearHand()
            
            
         
        
    def newDeck(self):
        '''
        If any cards were discarded, it is added back to the deck and shuffled.
        The discarded pile will now be empty
        
        '''
        for discarded_card in self.__discardPile:               
            self.__deck.addCard(discarded_card)
       
        self.__discardPile = []    
        self.__deck.shuffle()
            
        
      
      
    
if __name__== '__main__':
    
    table = Table()
    
    
    EndGame = False   
    print('*******************')
    print('Welcome to BACCARAT')
    print('*******************')    
    
    table.populateDeck()
    
    
    
    
    round_ended = False
    player = 0
    
    round_count = 1  
    
    while not EndGame:
        #----this marks the beginning of a round---
        print('\n')
        
        print('ROUND ', round_count)
        #deals out two cards to player and dealer 
        table.deal(0)
        table.deal(1)
        table.deal(0)
        table.deal(1)
        
        #displays the initial 2 cards/player
        table.displayTable()
        
        
        
        #check if it is a natural
        
        #takes in last digit of score
        player_score = ((table.checkTableValues()[0]) % 10)
        dealer_score = ((table.checkTableValues()[1]) % 10)
        
        if ((player_score == 8) or (player_score == 9)) or ((dealer_score == 8 )or (dealer_score == 9)):
            #check for tie
            if player_score == dealer_score:
                print('NATURAL! Round {} is a tie!', round_count)
                print('**********')
            
            elif player_score > dealer_score:
                print('NATURAL! Player wins round', round_count)
                print('**********')
                
            elif player_score < dealer_score:
                print('NATURAL! Dealer wins round', round_count)
                print('**********')
            
                
            table.clearTable()
            
            #RESTART PROMPTCOPY 1/3
            round_count += 1
            restart_prompt = input('Play another round? (Y/N)')
            if restart_prompt.lower() != 'y':
                EndGame = True
            
            
            if (restart_prompt.lower() == 'y') and (table.cardsRemaining() < 6):
                print('Not enought cards for another round. Creating a new deck.')
                table.newDeck()
                
        
        
        
        
        #---------third card dealing (only goes thru if natural number values were not attained)
        
        
        #checks if player gets card, do the complicated asf dealer rules a-f
        elif player_score <= 5:
            player = 0
            third_player_card = str(table.deal(player))#player DOES get a card
            
            #for rank checking:
            ranklist = []
            for i in third_player_card:
                ranklist.append(i)
                ranked = (ranklist[0])
                       
            #------------------
            
            player_score = ((table.checkTableValues()[0]) % 10)
            
            if dealer_score <= 2:
                player = 1
                third_dealer_card = str(table.deal(player))
                print('Player draws ', third_player_card) 
                print('Dealer draws ', third_dealer_card)
                
            elif dealer_score == 3 and ranked == '8':
                player = 1
                third_dealer_card = str(table.deal(player))
                print('Player draws ', third_player_card)
                print('Dealer draws ', third_dealer_card)
                
            elif (dealer_score == 4) and ((ranked == '2') or (ranked == '3') or (ranked == '4') or (ranked == '5') or (ranked == '6') or (ranked == '7')):
                player = 1
                third_dealer_card = str(table.deal(player))
                print('Player draws ', third_player_card)
                print('Dealer draws ', third_dealer_card)  
                
            elif (dealer_score == 5) and ((ranked == '4') or (ranked == '5') or (ranked == '6') or (ranked == '7')):
                player = 1
                third_dealer_card = str(table.deal(player))
                print('Player draws ', third_player_card)
                print('Dealer draws ', third_dealer_card)                                          
            elif (dealer_score == 6) and ((ranked == '6') or (ranked == '7')):
                player = 1
                third_dealer_card = str(table.deal(player))
                print('Player draws ', third_player_card)
                print('Dealer draws ', third_dealer_card) 
                
            elif (dealer_score == 7):
                print('Player draws ', third_player_card)
                print('Dealer stands')
            
            else:
                print('Player draws ', third_player_card)
                print('Dealer stands')
            
                
                #update scores because of new cards for dealer
            dealer_score = ((table.checkTableValues()[1]) % 10)
            
            table.displayTable()

            if player_score > dealer_score:
                print('Player wins round',round_count)
                print('**********')
                table.clearTable()
                    
            elif player_score < dealer_score:
                print('Dealer wins round', round_count)
                print('**********')
                table.clearTable()
                    
            elif player_score == dealer_score:
                print('Round {} ends in a tie!', round_count)
                print('**********')
                table.clearTable()                     
            
            #RESTART PROMPTCOPY 2/3
            round_count += 1
            restart_prompt = input('Play another round? (Y/N)')
                               
            if restart_prompt.lower() != 'y':
                    EndGame = True                   
        
            if (restart_prompt.lower() == 'y') and (table.cardsRemaining() < 6):
                print('Not enought cards for another round. Creating a new deck.')
                table.newDeck() 
       
       
        
            
 #-------------------------------------------------------------------------           
        #IF THE PLAYER STANDS: FOLLOW THE TWO DEALER RULES        
        elif (player_score == 6) or (player_score == 7):
            
            #1) dealer gets 3rd card            
            if dealer_score <= 5:
                player = 1
                dealer_third_card = str(table.deal(player))
                print('Player stands')
                print('Dealer draws ', dealer_third_card)
                
                #scores updated for who won loops since dealer gets a card
                dealer_score = ((table.checkTableValues()[1]) % 10)
                
            #2) dealer will stand also    
            elif (dealer_score == 6) or (dealer_score == 7):
                print('Player stands')
                print('Dealer stands')
                
            table.displayTable()
                
            #!!!!!!!!!!!!!!!who won loops!!!!!!!!!!!!!!!!!
            if player_score > dealer_score:
                print('Player wins round ',round_count)
                print('**********')
                table.clearTable()
                    
            elif player_score < dealer_score:
                print('Dealer wins round ', round_count)
                print('**********')
                table.clearTable()
                    
            elif player_score == dealer_score:
                print('Round {} ends in a tie!', round_count)
                print('**********')
                table.clearTable()                     
            
            #RESTART PROMPTCOPY 3/3
            round_count += 1
            restart_prompt = input('Play another round? (Y/N)')
                               
            if restart_prompt.lower() != 'y':
                    EndGame = True                   
        
            if (restart_prompt.lower() == 'y') and (table.cardsRemaining() < 6):
                print('Not enought cards for another round. Creating a new deck.')
                table.newDeck() 
                
                
           
           
           
           
           
           
           
           
                     
            
        
        
        
    print('Thanks for playing...Goodbye!')
    
