"""
Created on Fri Mar  6 20:47:18 2020

@author: Kyle
"""

import copy

from PlayerOne import player1
from PlayerTwo import player2
from Rules import Rules
        
        
    
"""
The class that controls the main logic of the game. Please don't change this code.
""" 
class GameManager():
    def __init__(self):
        self.player1Turn = False
        self.isGameOver = False
        self.p1 = player1()
        self.p2 = player2()
        self.b1 = []
        self.b2 = []
        self.b1Copy = []
        self.b2Copy = []
        self.p1Moves = []
        self.p2Moves = []
        self.r = Rules()
        
    #initializes one game, checks validity of piece placement
    #returns 1 if player one wins, returns 0 if player 2 wins    
    def startGame(self):
        self.isGameOver = False
        
        #initialize player1
        self.p1.amIFirst = self.player1Turn
        self.p1.startGame()
        self.b1 = copy.deepcopy(self.p1.pieces)
        self.b1Copy = copy.deepcopy(self.b1)
        #check placement of player_ones pieces
        if(not self.r.checkPieces(self.b1)):
            print("Invalid piece placement, Player 1 forfeited this game")
            self.gameOver()
            return 0
        
        #initialize player2
        self.p2.amIFirst = not self.player1Turn
        self.p2.startGame()
        self.b2 = copy.deepcopy(self.p2.pieces)
        self.b2Copy = copy.deepcopy(self.b2)
        #check placement of player_two pieces
        if(not self.r.checkPieces(self.b2)):
            print("Invalid piece placement, Player 2 forfeited this game")
            self.gameOver()
            return 1
        
        return self.play()
        
    #runs one game, when the game is over it calls the gameOver method then 
    #returns 1 or 0 depending on who won
    def play(self):
        #run till game is over
        while(not self.isGameOver):
            self.playerShoot()
        
        self.gameOver()
        #if it is my turn to shoot, but the game is over, then I lost
        if(self.player1Turn):
            return 0
        else:
            return 1
        
    #Let a player shoot, Check whether the shot hit or missed
    def playerShoot(self):            
        if(self.player1Turn):
            [i,j] = self.p1.makeMove()
            #save move for later analysis
            self.p1Moves.append([i,j])
            #Let player know whether their shot hit missed or sunk
            self.p1.lastMoveResult = self.checkShot(i,j,self.b2)
        else:
            [i,j] = self.p2.makeMove()
            self.p2.lastMoveResult = self.checkShot(i,j,self.b1)
            self.p2Moves.append([i,j])
        self.player1Turn = not self.player1Turn
        
    #check whether a shot hit missed or sunk
    def checkShot(self, row, col, pieces):
        #check each piece
        for p in pieces:
            #check if shot coordinates are contained in that piece
            if [row, col] in p:
                #remove coordinate from the piece
                p.remove([row, col])
                #if piece contains no more coordinates then that ship has sunk
                if len(p) == 0:
                    pieces.remove(p)
                    #if pieces is empty than all the ships have been sunk
                    if len(pieces) == 0:
                        self.isGameOver = True
                    return -1 #return sunk
                return 1 # return hit
        return 0 #return missed
    
    #Give each player the data from the other player so they can analyze it if they choose for better
    #play in the future.
    def gameOver(self):
        self.p1.gameOver(self.b2Copy, self.p2Moves)
        self.p2.gameOver(self.b1Copy, self.p1Moves)