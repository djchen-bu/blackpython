# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:28:07 2016

@author: ASS
"""
import sys
import random
from datetime import datetime

class cards():
    def start(self):
        klist = ['d']*13+['c']*13+['h']*13+['s']*13
        number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']*4
        keys = list(zip(klist,number))
        values = [4]*52
        ddict = dict(zip(keys,values))
        self.ddict = ddict
    def deal(self): #hands out card
        random.seed(datetime.now()) #generates random seed based on time
        keylist = list(self.ddict.keys())
        rip = random.sample(keylist,1)
        cards.remove(self,rip)
        return rip
    def checkhand(self,hand):    #checks value of hand
        total = 0
        acecheck = False
        for i in hand:
            if i[0][1] == 'J' or i[0][1] == 'Q' or i[0][1] == 'K':
                total += 10
            elif i[0][1] == "A":
                total += 11
                acecheck = True
            else:
                total += int(i[0][1])
        if acecheck == True and total > 21 or total == 17:
            total -= 10
        return total
            
    def checkdeck(self):    #checks how many cards are left
        return(sum(self.ddict.values()))
    def remove(self,victim):   #removes cards from dictionary at the end of round
        self.ddict[victim[0]] -= 1
        if self.ddict[victim[0]] == 0:
            del self.ddict[victim[0]]
        
class dealer(cards): #defines dealer logic
    def __init__(self,ddeal):
        self.ddeal = ddeal
        self.dhand = [self.ddeal,self.ddeal]
    def check(self,ddeal, hand, thold = 17):
        total = hand #self.d.checkhand(self.dhand)
        if total > 21:
            return(0)
        elif total < thold:
            self.dhand.append(ddeal)
            self.check(ddeal,hand)
        else:
            return(total)
    
class player(cards): #defines player logic
    def __init__(self,ddeal):
        self.ddeal = ddeal
        self.phand = [self.ddeal,self.ddeal]
    def check(self,ddeal,hand,thold = 17):
        total = hand #self.p.checkhand(self.phand)
        if total > 21 or total == 0:
            return(0)
        elif total < thold:
            self.phand.append(ddeal)
            self.check(ddeal,hand)
        else:
            return(total)
class gameplay(player,dealer):
    def __init__(self):
        self.c = cards()
        self.c.start()
        self.pscore = 0
        self.dscore = 0
        self.total = 0
    def dealing(self):
        if self.c.checkdeck() < 10:
            sys.exit(self.pscore/self.total,self.dscore/self.total)
    def checkwinner(self,p,d):
        if p.check(self.c.deal(),self.c.checkhand(p.phand)) > d.check(self.c.deal(),self.c.checkhand(d.dhand)):
            self.pscore += 1
            self.total += 1
        elif p.check(self.c.deal(),self.c.checkhand(p.phand)) < d.check(self.c.deal(),self.c.checkhand(d.dhand)):
            self.dscore += 1
            self.total += 1
        else:
            self.total += 1

#    def scoreboard(self, dealerscore = 0, playerscore = 0):
#        
#        
a = gameplay()
c = cards()
while True:
    a.dealing()
    d = dealer(c)
    p = player(c)
    a.checkwinner(p,d)