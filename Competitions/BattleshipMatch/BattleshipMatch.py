# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:47:18 2020

@author: Kyle
"""


from Battleship import GameManager

game = GameManager()

wins = 0
player1First = 0
#Run up to 1001 games, to ensure no tie
for nGames in range(1,1002):
    #number of wins for first player
    wins += game.startGame()
    #second player has won nGames - wins
    
    if game.player1Turn:
        player1First = player1First + 1
    
    #if more than one hundred games first one to win 500 games wins match
    if nGames > 100:
        if wins > 500:
            break
        elif nGames - wins > 500:
            break
    #If someone wins more than 70 of the first 100 games they are the winner
    elif nGames > 70:
        if wins > 70:
            break
        elif nGames - wins > 70:
            break
    #If someone wins the first 10 matches they are the winner
    elif nGames == 10:
        if wins == 10:
            break
        elif wins == 0:
            break
        
loss = nGames - wins
if wins > loss:
    print("Player 1 wins after", nGames, "games")
else:
    print("Player 2 wins after", nGames, "games")
    
print("player 1 went first ", player1First)

    


