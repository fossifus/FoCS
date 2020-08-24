# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:55:12 2020

@author: Kyle
"""

"""
The class that contains the rules for placing your pieces you may use this to check your piece placement
But do not change this code
"""
class Rules: 
    def checkPieces(self, pieces):
        for p in pieces:
            for [i,j] in p:
                if i < 0 or i > 9 or j < 0 or j > 9:
                    return False
            if not self.checkLinearity(p):
                return False
        if not self.checkSizes(pieces):
            return False
        return self.checkOverlap(pieces)
    
    def checkLinearity(self, piece):
        row = 0
        col = 0
        for [i,j] in piece[1:]:
            r = abs(piece[0][0] - i)
            c = abs(piece[0][1] - j)
            if r == 0:
                if not row == 0:
                    return False
                if not c == col + 1:
                    return False
                col += 1
            elif c == 0:
                if not col == 0:
                    return False
                if not r == row + 1:
                    return False
                row += 1
            else:
                return False
        return True
    
    def checkSizes(self, pieces):
        sizes = [2,3,3,4,5]
        if not len(pieces) == 5:
            return False
        s = [len(p) for p in pieces]
        s.sort()
        for i in range(5):
            if not sizes[i] == s[i]:
                return False
        return True    
    
    def checkOverlap(self, pieces):
        for piece in pieces:
            for [i,j] in piece:
                count = 0
                for p in pieces:
                    count += p.count([i,j])
                if not count == 1:
                    return False
        return True