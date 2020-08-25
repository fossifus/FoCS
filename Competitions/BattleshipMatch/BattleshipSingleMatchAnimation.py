# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:47:18 2020

Code for showing a single Battleship match, currently require package XXX


@author: Kyle
"""




import matplotlib.pyplot as plt
from matplotlib import animation
from Battleship import GameManager
import numpy as np






def placePiece(piece, Board):
    col = [i for [i,j] in piece]
    row = [j for [i,j] in piece]
    t = max(col)
    b = min(col)
    l = min(row)
    r = max(row)
    Board[b*10 + 2:t*10+9,l*10 + 2:r*10+9] = np.ones((10*(t-b)+7,10*(r-l)+7),dtype = int)*5

def init():
    return [im]


def GameOver():
    b = np.ones((100,210), dtype = int)*10
    b[50:90,10:20] = np.ones((40,10), dtype = int)*5
    b[80:90,20:40] = np.ones((10,20), dtype = int)*5
    b[70:80,30:40] = np.ones((10,10), dtype = int)*5
    b[50:60,20:40] = np.ones((10,20), dtype = int)*5
    
    return b

def animate(i):
    if i % 2 == 0:
        [r,c] = game.p1Moves[int(i/2)]
        B[r*10 + 3:r*10+8, c*10 + 3:c*10+8] = np.ones((5,5), dtype = int)
    else:
        [r,c] = game.p2Moves[int((i-1)/2)]
        A[r*10 + 3:r*10+8, c*10 + 3:c*10+8] = np.ones((5,5), dtype = int)
        
    Board = np.concatenate((A,np.ones((100,10), dtype = int),B),axis = 1)
    im = plt.imshow(Board)
    return [im]

game = GameManager()
game.startGame()

#Set up the Boards A and B
A = np.ones((100,100), dtype = int)*10
for i in range(1,10):
    A[:,i*10] = np.ones(100)
    A[i*10,:] = np.ones(100)
B = np.copy(A)

for p in game.b1Copy:
    placePiece(p,A)
for p in game.b2Copy:
    placePiece(p,B)

Board = np.concatenate((A,np.ones((100,10), dtype = int),B),axis = 1)


fig = plt.figure()
ax = plt.axes(xlim=(0, 210), ylim=(0, 100))
im = plt.imshow(Board)
#plt.show()

frame = len(game.p1Moves) + len(game.p2Moves)+1
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frame, interval=500, blit=True)
anim.save("Battleship.mp4")