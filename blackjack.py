# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:28:07 2016

@author: ASS
"""
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
        keylist = self.ddict.keys()
        rip = random.sample(keylist,1)
        cards.remove(self,rip)
        return rip
    def checkhand(self,hand):    #checks value of hand
        total = 0
        acecheck = False
        for i in hand:
            if i[1] in ("J","Q","K"):
                total += 10
            elif i[1] == "A":
                total += 11
                acecheck = True
            else:
                total += int(i[1])
        if acecheck == True and total > 21 or total == 17:
            total -= 10
        return total
            
    def checkdeck(self):    #checks how many cards are left
        print(sum(self.ddict.values()))
    def remove(self,victim):   #removes cards from dictionary at the end of round
        self.ddict[victim[0]] -= 1
        if self.ddict[victim[0]] == 0:
            del self.ddict[victim[0]]
        
class dealer(): #defines dealer logic
    def __init__(self):
        d = cards()
        self.dhand = [d.deal(),d.deal()]
    def check(self, thold = 17):
        total = cards.checkhand(self,self.dhand)
        if total > 21:
            return False
        elif total < thold:
            self.dhand.append(cards.deal())
            return("hit")
        else:
            return True
    
class player(): #defines player logic
    def __init__(self):
        p = cards()
        self.phand = [p.deal(),p.deal()]
    def check(self,thold = 17):
        total = cards.checkhand(self,self.phand)
        if total > 21:
            return False
        elif total < thold:
            self.phand.append(cards.deal())
            return("hit")
        else:
            return True
class gameplay():
    def __init__(self):
        self.g = cards()
        self.g.start()
        self.d = dealer()
        self.p = player()
    def checkplayer(self):
        chk = self.p.check()
        if chk == "hit":
            gameplay.checkplayer()
        elif chk == False:
            self.phand = {('0','0'):0}
            return False
        elif chk == True:
            return True
        print(self.g.checkhand(self.phand))


#    def scoreboard(self, dealerscore = 0, playerscore = 0):
#        
#        
a = gameplay()
a.checkplayer()