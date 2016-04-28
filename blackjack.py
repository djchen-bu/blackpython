# -*- coding: utf-8 -*-

import random
from datetime import datetime

class cards():
    def __init__(self,deck = 7):    #makes the deck
        klist = ['d']*13+['c']*13+['h']*13+['s']*13
        number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']*4
        keys = list(zip(klist,number))  #keys are made up of the suit and the value
        values = [deck]*52      #dictionary values are the number of cards
        ddict = dict(zip(keys,values))
        self.ddict = ddict
    def deal(self): #hands out card
        random.seed(datetime.now()) #generates random seed based on time
        keylist = list(self.ddict.keys())   
        rip = random.sample(keylist,1)  #picks random dictionary value
        cards.remove(self,rip)  #removes card from dicitonary
        return rip
    def checkhand(self,hand):    #checks value of hand
        total = 0
        acecheck = False
        for i in hand:  #adds up value of the cards
            if i[0][1] == 'J' or i[0][1] == 'Q' or i[0][1] == 'K':
                total += 10
            elif i[0][1] == 'A':    #automatically adds 11 if ace
                total += 11
                acecheck = True
            else:
                total += int(i[0][1])
        if acecheck == True and total > 21 or total == 17:  #checks if, when the ace value is 11, it is over 21 it will subtract 10
            total -= 10
        return total
            
    def checkdeck(self):    #checks how many cards are left
        return(sum(self.ddict.values()))    
    def remove(self,victim):   #removes cards from dictionary at the end of round
        self.ddict[victim[0]] -= 1
        if self.ddict[victim[0]] == 0:  #checks if there is anymore cards of that suit and value
            del self.ddict[victim[0]]
        
class dealer(cards): #defines dealer logic
    def __init__(self,c1,c2):
        self.dhand = [c1,c2]
    def check(self,ddeal, total):   #checks if their hand is under 17 and if so it adds another card and checks again
        if total < 17:
            self.dhand.append(ddeal)
            return self.dhand
        elif total > 21:
            return(0)
        else:
            return(total)
    
class player(cards): #defines player logic identical with dealer
    def __init__(self,c1,c2):
        self.phand = [c1,c2]
    def check(self,ddeal,total):
        if total < 17:
            self.phand.append(ddeal)
            return self.phand
        elif total > 21:
            return(0)
        else:
            return(total)
class gameplay(player,dealer):
    def __init__(self,deck):
        self.c = cards(deck)
    def checkplayer(self,p,phand):  #checks if the return from pcheck return a list which shows that it needs to hit or deal another card.
        pscore = p.check(self.c.deal(),self.c.checkhand(phand))
        if type(pscore) ==  list:
            self.checkplayer(p,pscore)
        else:
            return(pscore)
            
    def checkdealer(self,d,dhand):  #same as the checkplayer above
        dscore = d.check(self.c.deal(),self.c.checkhand(dhand))
        if type(dscore) ==  list:
            self.checkdealer(d,dscore)
        else:
            return(dscore)   

a = gameplay(20)
pscore = 0
dscore = 0
total = 0
while a.c.checkdeck() > 20: #runs loop as long as there are at least 20 cards in the deck
    d = dealer(a.c.deal(),a.c.deal())
    p = player(a.c.deal(),a.c.deal())
    total += 1
    a.checkplayer(p,p.phand)
    a.checkdealer(d,d.dhand)
    if a.checkplayer(p,p.phand) > a.checkdealer(d,d.dhand): #gives a point to player if their score is higher than the dealer
        pscore += 1
    if a.checkplayer(p,p.phand) < a.checkdealer(d,d.dhand): #vice versa
        dscore += 1
print("player win percentage:{} dealer win percentage:{}".format(pscore/total,dscore/total))