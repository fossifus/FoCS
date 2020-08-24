# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:49:11 2020

@author: Kyle
"""

#from AITemplate import AIPlayer
#
#"""
#CHANGE THIS CODE
#First player logic goes in this class
#You can override any and all of the functions of the parrent class to improve upon basic gameplay
#Make sure to call your own placePieces method from the startGame method
#You are also welcome to create your own methods or even read and write to a file.
#"""
#class player1(AIPlayer):
#    #This method is only called once at the beginning of each match. It is not called between each game
#    def __init__(self):
#        super().__init__()
#        #Good place to define any variables you want to use throughout each match
#    
#    #startGame
#    #placePieces(self):
#    #makeMove(self):
#    #gameOver(self):




from Rules import Rules
from AITemplate import AIPlayer

"""
CHANGE THIS CODE
First player logic goes in this class
You can override any and all of the functions of the parrent class to improve upon basic gameplay
Make sure to call your own placePieces method from the startGame method
You are also welcome to create your own methods or even read and write to a file.
"""
class player1(AIPlayer):
    #This method is only called once at the beginning of each match. It is not called between each game
    def __init__(self):
        super().__init__()
        self.r = Rules()
        self.moves = []
        self.hitOnce = False
        self.nextMoves = []
        self.lastHits = []
        #Good place to define any variables you want to use throughout each match
    
    def randomMove(self):
        move = [5,5]
        while move in self.moves:
            move = super().makeMove()
        return move
    
    def startGame(self):
        super().startGame()
        self.moves = []
        self.hitOnce = False
        self.nextMoves = []
        self.lastHits = []
    
    def makeMove(self):
        shot = []
        if self.lastMoveResult == 0:
            if len(self.nextMoves) == 0:
                if len(self.lastHits) == 0:
                    shot = self.randomMove()
                else:
                    [i,j] = self.lastHits.pop()
                    self.hitOnce = False
                    if j > 1:
                        self.nextMoves.append([i,j-2])
                    if j < 8:
                        self.nextMoves.append([i,j+2])
                    if i > 1:
                        self.nextMoves.append([i-2,j])
                    if i < 8:
                        self.nextMoves.append([i+2,j])
                    shot = self.nextMoves.pop()
            else:
                shot = self.nextMoves.pop()
        if self.lastMoveResult == -1:
            self.nextMoves = []
            self.lastHits = []
            self.hitOnce = False
            shot = self.randomMove()
        if self.lastMoveResult == 1:
            self.lastHits.append(self.moves[-1])
            if self.hitOnce:
                i = 2*self.lastHits[-1][0] - self.lastHits[-2][0]
                j = 2*self.lastHits[-1][1] - self.lastHits[-2][1]
                self.nextMoves.append([i,j])
            else:
                [i,j] = self.moves[-1]
                if j > 0:
                    self.nextMoves.append([i,j-1])
                if j < 9:
                    self.nextMoves.append([i,j+1])
                if i > 0:
                    self.nextMoves.append([i-1,j])
                if i < 9:
                    self.nextMoves.append([i+1,j])
            shot = self.nextMoves.pop()
            self.hitOnce = True
            
        self.moves.append(shot)
        return shot
        
    #gameOver(self):
    
    
    
    
#ships = [[1,3],[1,4],[1,5],[1,6]]
#p1 = player1()
#p1.startGame()
#while True:
#    move = p1.makeMove()
#    if move in ships:
#        ships.remove(move)
#        p1.lastMoveResult = 1
#    else:
#        p1.lastMoveResult = 0