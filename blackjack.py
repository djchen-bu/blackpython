# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:28:07 2016

@author: ASS
"""

class gameplay():
    def __init__(self,deck = 4):
        klist = ['d']*13+['c']*13+['h']*13+['s']*13
        number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']*4
        keys = list(zip(klist,number))
        values = [deck]*52
        ddict = dict(zip(keys,values))
        
    def hit(self):
        
    def stand(self):
        
    def check(self):
        

class dealer(deck):
    print('ass')
class player(deck):
    print('assbeef')
