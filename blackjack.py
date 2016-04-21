# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:28:07 2016

@author: ASS
"""
import random

class cards():
    def __init__(self,deck = 4):
        klist = ['d']*13+['c']*13+['h']*13+['s']*13
        number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']*4
        keys = list(zip(klist,number))
        values = [deck]*52
        ddict = dict(zip(keys,values))
        self.ddict = ddict
    def deal(self): #hands out card
        testlist = ddict.keys()
        
        print(random.sample(testlist,2))    #testing out dealing
#    def hit(self):  #draws card
#        
#    def stand(self):    #ends turn
#        
#    def checkhand(self):    #checks value of hand
#        
#    def checkdeck(self):    #checks how many cards are left
#        
#    def remove(self):   #removes cards from dictionary at the end of round
#
#class dealer(cards): #defines dealer logic
#    def __init__(self):
#        dhand = cards.deal()
#    
#class player(cards): #defines player logic
#    print('assbeef')
#class gameplay(cards,dealer,player):
#
#
#
#    def scoreboard(self, dealerscore = 0, playerscore = 0):
#        
        
a = cards()
a.deal()