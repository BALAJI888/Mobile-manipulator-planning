# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:45:50 2023

@author: Bijo Sebastian
"""
import time
start_time = time.time()
import Routing2
import copy
import Map
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# global count
# count = 0
class Maze:
  """
  This class outlines the structure of the maze problem
  """
  
  maze_map = []# To store map data, start and goal points
  
  # Legal moves
  # [delta_x, delta_y, description]
  eight_neighbor_actions = {'up':[-1, 0], 'down':[1, 0], 'left': [0, -1], 'right': [0, 1],"upleft":[-1,-1],"upright":[-1,1],"downleft":[1,-1],"downright":[1,1]}
  
  map_plot_copy = []
  plot_colormap_norm = matplotlib.colors.Normalize(vmin=0.0, vmax=19.0)
  fig,ax = plt.subplots(1)
  plt.axis('equal')
  
  def plot_map(self):
      """
      Plot
      """
      start = self.getStartState()
      goal = self.getGoalState()
      self.map_plot_copy[start[0]][start[1]] = Map.start_id
      self.map_plot_copy[goal[0]][goal[1]] = Map.goal_id
      plt.imshow(self.map_plot_copy, cmap=plt.cm.tab20c, norm=self.plot_colormap_norm)
      #plt.savefig("D:/SEM 06/ED5215/Project/Final_presentation_pics/5 objects/" + str(count))
      plt.show()
      
      
  # default constructor
  def __init__(self, id):
      """
      Sets the map as defined in file Map
      """
      #Set up the map to be used
      self.maze_map = Map.maps_dictionary[id]
      self.map_plot_copy = copy.deepcopy(self.maze_map.map_data)
      self.plot_map()
      return
     
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     start_state = self.maze_map.start
     return start_state
 
  def getGoalState(self):
     """
     Returns the start state for the search problem 
     """
     goal_state =  self.maze_map.goal
     return goal_state
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     if state == self.getGoalState():
         return True
     else:
         return False

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     #Update changes on the plot copy
     self.map_plot_copy[state[0]][state[1]] = Map.expanded_id
     successors = []
     for action in self.eight_neighbor_actions:
         
         #Get indiivdual action
         del_x, del_y = self.eight_neighbor_actions.get(action)
         
         #Get successor
         new_successor = [state[0] + del_x , state[1] + del_y] + state[2:]
         new_action = action
         
         
         # Check for obstacle
         
         if self.maze_map.map_data[new_successor[0]][new_successor[1]] == Map.obstacle_id:
             continue
         
         if state[6] != 3:
             if self.maze_map.map_data[new_successor[0]][new_successor[1]] == Map.beacon_id1 and not(new_successor[2]):
                 new_successor[6] = new_successor[6] + 1
                 new_successor[2] = True
             elif self.maze_map.map_data[new_successor[0]][new_successor[1]] == Map.beacon_id2 and not(new_successor[3]):
                 new_successor[6] = new_successor[6] + 1
                 new_successor[3] = True
             elif self.maze_map.map_data[new_successor[0]][new_successor[1]] == Map.beacon_id3 and not(new_successor[4]):
                 new_successor[6] = new_successor[6] + 1
                 new_successor[4] = True
             elif self.maze_map.map_data[new_successor[0]][new_successor[1]] == Map.beacon_id4 and not(new_successor[5]):
                 new_successor[6] = new_successor[6] + 1
                 new_successor[5] = True
         if self.maze_map.map_data[new_successor[0]][new_successor[1]] == Map.goal_id:
                 new_successor[6] = 0
             
         #Update changes on the plot copy
         if self.map_plot_copy[new_successor[0]][new_successor[1]] != Map.expanded_id:
             self.map_plot_copy[new_successor[0]][new_successor[1]] = Map.fringe_id
         
         #Check cost
         if self.maze_map.map_data[new_successor[0]][new_successor[1]] == Map.free_space_id2:
             new_cost = Map.free_space_id2_cost
         elif action in ["upleft","upright","downleft","downright"]:
             new_cost = 1.414
         else:
             new_cost = Map.free_space_id1_cost 
             
         successors.append([new_successor, new_action, new_cost])
         
     #Plot the changes
     #self.plot_map()
     return successors

if __name__ == '__main__':
    
    current_maze = Maze(1)
    path = Routing2.aStar(current_maze)
    
    if path:
        #print('Found a path of %d moves: %s' % (len(path), str(path))) 
        #Display solution
        row,col = current_maze.getStartState()[0:2]
        path_states = [] 
        for action in path:
            del_x, del_y = current_maze.eight_neighbor_actions.get(action)
            newrow = row + del_x
            newcol = col + del_y
            path_states.append([newrow,newcol])
            #Update changes on the plot copy
            if [newrow , newcol] == [10,10]:
                current_maze.map_plot_copy[newrow][newcol] = 4
            elif [newrow , newcol] == [2,4]:
                current_maze.map_plot_copy[newrow][newcol] = 4
            elif [newrow , newcol] == [12,18]:
                current_maze.map_plot_copy[newrow][newcol] = 4
            elif [newrow , newcol] == [16,9]:
                current_maze.map_plot_copy[newrow][newcol] = 4
            else:
                current_maze.map_plot_copy[newrow][newcol] = 10
            # count = count +1
            row = newrow
            col = newcol
            #current_maze.plot_map()
        #Plot the solution
    else:
        print("Could not find a path")

Final_path_states = []
for element in path_states:
    a = [element[0],element[1],1]
    R1 = [[0,1,-10],[-1,0,10],[0,0,1]]
    NC = np.matmul(R1,a)
    NC = NC/2
    Final_path_states.append([NC[0],NC[1]])
print(Final_path_states)
print("--- %s seconds ---" % (time.time() - start_time))
