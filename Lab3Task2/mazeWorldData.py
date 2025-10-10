import random

actions = ["left","right","advance"]

maze = [[1,0,1,1,1,0,"end"],
        [1,1,0,0,0,1,1],
        [1,1,1,0,1,1,1],
        [0,1,0,1,0,1,0],
        [1,1,1,0,1,1,1],
        [1,1,0,1,0,1,1],
        ["start",0,0,1,0,0,1]]

treasures = ["diamond","gold","pizza","points"]

for i in treasures:
    a = random.randint(0,6)
    b = random.randint(0,6)
    while maze[a][b] != 1:
        a = random.randint(0,6)
        b = random.randint(0,6)
    maze[a][b] = i

#print(maze)

mazeActions = {
    (0,0):{},
    (0,2):{"advance":(2,2),"left":(0,0),"right":(0,3)},
    (0,3):{"advance":(3,3),"left":(0,2),"right":(0,4)},
    (0,4):{"advance":(2,4),"left":(0,3),"right":(0,6)},
    (0,6):{},
    (1,0):{"advance":(2,0)},
    (1,1):{"advance":(1,0)},
    (1,5):{"advance":(1,7)},
    (1,6):{"advance":(2,7)},
    (2,0):{},
    (2,1):{"left":(1,1),"right":(2,2)},
    (2,2):{"advance":(0,2)},
    (2,4):{"advance":(0,4)},
    (2,5):{"left":(2,4),"right":(1,5)},
    (2,6):{},
    (3,1):{"left":(2,1),"right":(3,3)},
    (3,3):{"advance":(0,3),"left":(3,1),"right":(3,5)},
    (3,5):{"left":(3,3),"right":(2,5)},
    (4,0):{},
    (4,1):{"left":(3,1),"right":(4,2)},
    (4,2):{},
    (4,4):{},
    (4,5):{"left":(4,4),"right":(3,5)},
    (4,6):{},
    (5,0):{"advance":(4,0)},
    (5,1):{"left":(5,0),"right":(4,1)},
    (5,3):{"left":(5,1),"right":(5,5)},
    (5,5):{"left":(4,5),"right":(5,6)},
    (5,6):{"advance":(4,6)},
    (6,0):{"advance"},
    (6,3):{"left":(5,3),"right":(6,6)},
    (6,6):{},
}


