# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 22:33:08 2023

@author: RAJBALAJ
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 12:16:30 2023

@author: Bijo Sebastian
"""

#Definitions based on color map
start_id = 1
goal_id = 8
obstacle_id = 16
beacon_id = 12
free_space_id1 = 3
free_space_id2 = 18
free_space_id1_cost = 1
free_space_id2_cost = 3
fringe_id = 4
expanded_id = 6



class Maps:
    """
    This class outlines the structure of the maps
    """    
    map_data = []
    start = []
    goal = []
    
#Maze maps
map_1 = Maps()
map_1.map_data = [
    [16,16,16,16,16,16,16,16,16,16,16],
    [16, 3, 3, 3,16,16,16,16, 3, 1,16],
    [16,16, 3, 3,16, 3, 3,16, 3,16,16],
    [16,16, 3, 3, 3, 3, 3, 3, 3,16,16],
    [16,16, 3,16,16,16,16,16, 3,16,16],
    [16, 3, 3, 3, 3, 3, 3, 3, 3,16,16],
    [16, 3,16, 3, 3, 3, 3, 3, 3,3,16],
    [16, 3,16,16,16,16, 3 ,3,16,16,16],
    [16, 3, 3, 3, 3,16, 3, 3,16, 3,16],
    [16, 3,16,16, 3, 3, 8, 3, 16, 3,16],
    [16,16,16,16,16,16,16,16,16,16,16],
     ]
map_1.start = [1,9]
map_1.goal =  [9,6]

maps_dictionary = {1:map_1}


 
