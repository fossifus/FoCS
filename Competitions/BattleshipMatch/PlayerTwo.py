# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:49:47 2020

@author: Kyle
"""

from AITemplate import AIPlayer


class player2(AIPlayer):
    #This method is only called once at the beginning of each match. It is not called between each game
    def __init__(self):
        super().__init__()
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
#        self.lastMoveResult = 0 #Miss = 0, Hit = 1, Sink = -1
        
        #place your pieces on the board
#        self.placePieces()
        
#    def placePieces(self):
#        Battleship = [[0,1],[0,2],[0,3],[0,4]]
#        ptBoat = [[0,5],[1,5]]
#        AircraftCarrier = [[0,9],[1,9],[2,9],[3,9],[4,9]]
#        Destroyer1 = [[9,0],[9,1],[9,2]]
#        Destroyer2 = [[9,5],[9,4],[9,3]]
#        #please note that the following code would not be a valid ship placement
#        #Destroyer2 = [[7,4],[7,5],[7,3]] #pieces need to be in order either forward or backward
#        
#        self.pieces = [Battleship, ptBoat, AircraftCarrier, Destroyer1, Destroyer2]
#    
    def makeMove(self):
        shot = []
        if self.lastMoveResult == 0:
            if len(self.nextMoves) == 0:
                 shot = self.randomMove()
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










#"""
#CHANGE THIS CODE
#An example of another players attempt at making the best battleship computer player
#You may use this class to help train your own AI
#"""
#class player2(AIPlayer):
#    def __init__(self):
#        super().__init__()
#        self.moves = []
#        
##    #Write your oponents code here
#    def makeMove(self):
#        [i,j] = [5,5]
#        while [i,j] in self.moves:
#            [i,j] = super().makeMove()
#        self.moves.append([i,j])
#        return [i,j]
#    
#    def startGame(self):
#        super().startGame()
#        self.moves = []    
    