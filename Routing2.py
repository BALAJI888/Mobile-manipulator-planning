# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 22:24:24 2023

@author: RAJBALAJ
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 22:33:33 2023

@author: RAJBALAJ
"""

import operator
import math
import numpy as np


def heuristic_1(problem, state):
    g = problem.getGoalState()
    h = math.sqrt((g[0]-state[0])**2 + (g[1] - state[1])**2)
    return h

def aStar(problem):
    fringe = []
    closed = []
    parent = {}
    S0 = problem.getStartState()
    S0 = [S0,"down",0]
    fringe.append(S0)
    def selectmin (d):
        n = 0
        min = d[0][2] + heuristic_1(problem, d[0][0])
        for j in range(1,len(d)):
            if min > d[j][2] + heuristic_1(problem, d[j][0]):
                min = d[j][2] + heuristic_1(problem, d[j][0])
                n = j
            else:
                continue
        return(d[n])
    
    while True:
        b = selectmin(fringe)
        fringe.remove(b)
        closed.append(b)       
        if b[0] == problem.getGoalState():
            break
        c = problem.getSuccessors(b[0])
        for element in c:
            count = 0
            f = len(fringe)
            element[2] = element[2] + b[2]
            for i in range(f):
                if element[0] == fringe[i][0]:
                    count = 1
                    if fringe[i][2] > element[2]:
                        fringe.remove(fringe[i])
                        fringe.append(element)
                        parent[tuple(element[0])] = b
                        break
                     
            if count == 1:
                continue
            e = len(closed)
            for j in range(e):
                if element[0] == closed[j][0]:
                    count = 2
            if count ==2:
                continue
            fringe.append(element)
            parent[tuple(element[0])] = b
    path = []
    t = b
    while True:
        path.append(t[1])
        t = parent[tuple(t[0])]
        if S0[0] == t[0]:
            break
    path.reverse()
    return(path)
    
  
   
  
    