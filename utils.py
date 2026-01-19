import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations
import io
import csv
import math
from pulp import *

import random
from typing import List, Tuple, Dict, Optional

def get_example(k) :
    examples = [
        [[5, 2, 2, 1, 1],
         [2, 5, 3, 2, 1],
         [2, 3, 5, 4, 1],
         [1, 2, 4, 5, 5],
         [1, 1, 1, 5, 5]],
        
        [[10, 4, 3, 2, 2],
         [4, 10, 6, 4, 2],
         [3, 6, 10, 8, 2],
         [2, 4, 8, 10, 10],
         [2, 2, 2, 10, 10]],

        [[10, 4, 3, 2],  
         [4, 10, 6, 4],  
         [3, 6, 10, 8],  
         [2, 4, 8, 10]],        
         
        [[2, 2, 1, 0, 0],
         [2, 2, 2, 1, 1],
         [1, 2, 2, 2, 1],
         [0, 1, 2, 2, 2],
         [0, 1, 1, 2, 2]],

        [[10,7, 6, 0, 0, 0, 0],
         [7,10, 7, 3, 2, 1, 1],
         [6, 7,10, 7, 2, 2, 1],
         [0, 3, 7, 10,3, 3, 3],
         [0, 2, 2, 3, 10,7, 5],
         [0, 1, 2, 3, 7, 10,6],
         [0, 1, 1, 3, 5, 6,10]],
    
        [[9,4,5,4,1], 
         [4,9,5,4,1], 
         [5,5,9,8,7], 
         [4,4,8,9,7],
         [1,1,7,7,9]]
        ]
    return(examples[k])

def compute_max_closer(distance_matrix) : #Function to compute the center matrix from a Robinson space
    n= len(distance_matrix)
    max_closer=np.zeros((n,n))
    # Compute hanging node distances
    hang_distance = [0]*n
    for i in range(n):
        for j in range(n):
            max_closer[i][j]=i
            increment=1 # left -> right
            if (i>j) :
                increment=-1 # right -> left
            for k in range(i,j,increment):
                if distance_matrix[i][k] < distance_matrix[k][j]:
                    max_closer[i][j] = k
                
    return max_closer

