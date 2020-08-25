# -*- coding: utf-8 -*-
"""

DON'T TOUCH THIS CLASS
Base Class for AI logic. Contains functionality to play a game of battleship.
You may modify the two child classes which inherit from this one

Created on Sat Mar 21 11:48:51 2020
@author: Kyle
"""


import numpy as np

class AIPlayer:
    #initialization of a player, this method is only called once, at the beginning of each match.
    #not between every game.
    def __init__(self):        
        #list of ships in ordered pair i.e. [[row, col], [row, col]], see place piece method
        self.pieces = []
        
        
    #A method to prepare for a new game
    #This method is called at the beginning of each game, so up to 1000 times in a single match
    def startGame(self):
        #The result of the last move, The game manager will update this after you make a shot
        self.lastMoveResult = 0 #Miss = 0, Hit = 1, Sink = -1
        
        #place your pieces on the board
        self.placePieces()
    
    #Basic function for making a shot
    #GameManager will call this method every time it is your turn.
    def makeMove(self):
        #Select a random row and column
        r = np.random.randint(10)
        c = np.random.randint(10)
        #Return the row and column numbers, The grid is 10X10 so numbers 0-9 are valid
        return [r,c]
    
    
    #Basic function for placing your pieces on the board at the beginning of the game
    def placePieces(self):
        Battleship = [[0,1],[0,2],[0,3],[0,4]]
        ptBoat = [[7,7],[8,7]]
        AircraftCarrier = [[0,9],[1,9],[2,9],[3,9],[4,9]]
        Destroyer1 = [[9,0],[9,1],[9,2]]
        Destroyer2 = [[7,5],[7,4],[7,3]]
        #please note that the following code would not be a valid ship placement
        #Destroyer2 = [[7,4],[7,5],[7,3]] #pieces need to be in order either forward or backward
        
        self.pieces = [Battleship, ptBoat, AircraftCarrier, Destroyer1, Destroyer2]
        
    #Function for game clean-up and analysis, not a necessary function for basic play but still
    #available for you to override
    def gameOver(self, opponentsPieces, opponentsShots):
        pass