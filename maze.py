import copy
import pygame
import time
import itertools
import numpy as np

WIDTH = 500
HEIGHT = 600

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
grid = []

class Node:
    newid = itertools.count()
    
    def __init__(self,x , y):
        self.id = next(Node.newid)
        #self.data = data
        self.x = x
        self.y = y
        self.parent = None
        self.offspring = None
        self.wall = False
        
        
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return str(self.data)
    
class Maze:
    def __init__(self):
       self.COL = 20
       self.ROW = 20
       self.CELL_SIZE = 19
       self.maze  = [
                        [1, 1, 0, 0, 1, 0, 0, 0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
                        [0, 1, 0, 0, 0, 1, 1, 1 ,0 ,1 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0],
                        [0, 0, 1, 1, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0],
                        [1, 0, 1, 0, 1, 1, 0, 0 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,1 ,0 ,1 ,0],
                        [0, 0, 0, 0, 0, 1, 1, 1 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,0],
                        [0, 1, 1, 1, 0, 0, 0, 0 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,0 ,0 ,0],
                        [0, 1, 1, 1, 0, 1, 1, 1 ,1 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,0],
                        [0, 0, 0, 1, 0, 0, 0, 0 ,1 ,0 ,0 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ,1 ,0],
                        [1, 1, 0, 1, 1, 1, 1, 1 ,1 ,0 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,0 ,1 ,1],
                        [1, 0, 0, 0, 0, 0, 1, 1 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,1 ,0 ,0 ,1 ,0],
                        [1, 0, 1, 1, 1, 0, 0, 0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,0],
                        [1, 0, 1, 0, 1, 1, 1, 0 ,1 ,0 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,1],
                        [0, 0, 1, 0, 0, 1, 0, 0 ,1 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,0],
                        [0, 1, 1, 1, 0, 1, 0, 1 ,0 ,0 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,0 ,1 ,0],
                        [0, 0, 0, 1, 0, 1, 0, 0 ,1 ,0 ,1 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0],
                        [1, 1, 0, 1, 0, 1, 0, 1 ,1 ,0 ,0 ,1 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,0],
                        [0, 0, 0, 1, 0, 1, 1, 1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ,1 ,0],
                        [0, 1, 1, 1, 0, 1, 0, 0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,1],
                        [0, 1, 0, 0, 0, 1, 0, 1 ,1 ,1 ,0 ,0 ,1 ,1 ,0 ,1 ,0 ,0 ,0 ,0],
                        [0, 0, 0, 1, 0, 0, 0, 1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1]
                    ]
       
    def build_grid(x, y, w):
        for i in range(1,21):
            x = 20                                                           
            y = y + 20                                                        
            for j in range(1, 21):
                pygame.draw.line(screen, WHITE, [x, y], [x + w, y])           
                pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   
                pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])  
                pygame.draw.line(screen, WHITE, [x, y + w], [x, y])           
                grid.append((x,y))                                            
                x = x + 20   
                
    def draw(self):
            x = 0
            y = 0
            for i in range(self.COL):
                    x = x + 20
                    for j in range(self.ROW):
                        y = y + 20
                        if (y > 400): y = 20
                        if (self.maze[j][i] == 1):
                            pygame.draw.rect(screen, BLUE, (x+1, y+1, self.CELL_SIZE-1, self.CELL_SIZE-1), 0)
                            pygame.display.update()
                            time.sleep(.001) 
                        if (self.maze[j][i] == 0):
                            pygame.draw.rect(screen, WHITE, (x+1, y+1, self.CELL_SIZE-1, self.CELL_SIZE), 0)
                            pygame.display.update()
                            time.sleep(.001) 
                        
            time.sleep(3)
     
    
def expand(edo_actual):
    retorno = []
    q = len(edo_actual.data)
    
    for i in range(q):
        edo_temp = copy.deepcopy(edo_actual)
        edo_value = edo_temp.data[i]+1
        
        if (edo_value <= (q)):
            edo_temp.data[i] = edo_temp.data[i]+1
            retorno.append(edo_temp)
           
    return retorno

#BUSQUEDA A LO ANCHO
def b_ancho(frontier):
    while True:
        if not frontier:
            return "solución no encontrada"
        edo_actual = frontier.pop(0)
        print(edo_actual)
        if(goalTest(edo_actual.data)):
            
            return "Solución encontrada en "+str(edo_actual.data)
        else:
            offspring = expand(edo_actual)
            #edo_actual.offspring=offspring
            
            if offspring :
                for i in offspring:
                    frontier.append(i)

if __name__ == "__main__": 
    m = Maze()
    m.build_grid(0,20)
    m.draw()