from src.mazeData import makeMaze
from src.mazeData import draw_maze
from src.mazeData import defineMazeAvailableActions
from src.mazeData import makeMazeTransformationModel
from src.mazeData import mazeStatesLocations
from src.mazeData import intTupleTostr
from src.graphProblemClass import GraphProblem
from src.maze2025GraphClass import mazeGraph
from pyvis.network import Network
from src.mazeProblemClass import MazeProblem
from src.nodeClass import Node
from src.ghostClass import Ghost
from src.foodPelletClass import FoodPellet
import math
from src.PS_agentPrograms import *
from src.agents import *
from src.naigationEnvironmentClass import MazeNavigationEnvironment

n=10
maze1=makeMaze(n)
print(maze1)
#draw_maze(maze1)
mazeAvalActs=defineMazeAvailableActions(maze1)
#print(mazeAvalActs)
mazeAvalActs[(7,3)] # correct: food is there, but it is possible to move L,U,R,D from it
#print(maze1[7,3])
maze1TM=makeMazeTransformationModel(mazeAvalActs)
#print(maze1TM)

#Making graph
mazeWorldGraph1 = mazeGraph(maze1TM)
#print(mazeWorldGraph1.graph_dict)
#mazeWorldGraph1.get((0,0))
#print(list(maze1TM.keys()))

mazeWorldGraph2 = mazeGraph(maze1TM, mazeStatesLocations(list(maze1TM.keys())))
#print(mazeWorldGraph2.nodes()[:5])
#print(mazeWorldGraph2.locations)
#print(mazeWorldGraph2.get((0, 1), (0,2)))

net_maze = Network( heading="Lab5. Examples of PacMan World",
                bgcolor ="#242020",
                font_color = "white",
                height = "750px",
                width = "100%",
                directed = True
) # do this
nodeColors={
    "wall":"red",
    "path": "white",
    "food":"yellow"
}

nodeColorsList=[]
for node in mazeWorldGraph2.origin.keys():
    if maze1[node[0],node[1]]==1:
        nodeColorsList.append(nodeColors["path"])
    elif maze1[node[0],node[1]]==2:
        nodeColorsList.append(nodeColors["food"])
    else:
        nodeColorsList.append(nodeColors["wall"])

nodes=["-".join(str(item) for item in el) for el in mazeWorldGraph2.origin.keys()]
x_coords = []
y_coords = []

for node in mazeWorldGraph2.origin.keys():
    x,y=mazeWorldGraph2.getLocation(node)
    x_coords.append(x)
    y_coords.append(y)

sizes=[10]*len(nodes)
#hidden labels, and hover titles
net_maze.add_nodes(nodes, color=nodeColorsList, x=x_coords, y=y_coords, size=sizes, title=nodes)
for node in net_maze.nodes:
    node['label']=''
#print(net_maze.nodes)
#print(mazeWorldGraph2.origin[(0,0)])
#print(mazeWorldGraph2.origin)
edge_weights = {(intTupleTostr(k), intTupleTostr(v2)) : k2 for k, v in mazeWorldGraph2.origin.items() for k2, v2 in v.items()}#actions
#print(edge_weights)
edges=[]
for node_source in mazeWorldGraph2.nodes():
    for node_target, action in mazeWorldGraph2.get(node_source).items():
        #node_target or node_source is a tuple -> convert to str
        if (intTupleTostr(node_source),intTupleTostr(node_target)) not in edges:
            net_maze.add_edge(intTupleTostr(node_source),intTupleTostr(node_target), title=edge_weights[(intTupleTostr(node_source),intTupleTostr(node_target))], smooth={"type": "curvedCW", "roundness": 0.2}, lable="")
            edges.append((intTupleTostr(node_source),intTupleTostr(node_target)))
# Enable dynamic edges for separate curved arrows.
#net_maze.set_edge_smooth('dynamic')
net_maze.toggle_physics(False)
#net_maze.show("graph1.html", notebook=False)


#--------------------------------------------------------------------

#initState, goalState=(0,1),(2,4)
initState = (0,1)
foodStates = []
for i in range(len(maze1)):
    for j in range(len(maze1[0])):
        if maze1[i][j] == 2:
            foodStates.append((i,j))
#print(foodStates)
goalState = []
currLoc = Node((0,1))
while foodStates != []:
    #currLoc = Node((0,1))
    h = 1000
    j = None
    
    for i in foodStates:
        #print(f"currLoc = {currLoc}, h={h}, j={j}, i={i}")
        tmp=currLoc.path_cost+abs(currLoc.state[0]-i[0])+abs(currLoc.state[1]-i[1])
        if tmp < h:
            h = tmp
            j = i
    currLoc = Node(j)
    goalState.append(j)
    if j != None:
        #print(foodStates)
        foodStates.remove(j)
#print(goalState)



    
#node.path_cost+abs(node.state[0]-problem.goal[0])+abs(node.state[1]-problem.goal[1])
mp1=MazeProblem(initState,goalState,mazeWorldGraph2)
testState=(0,2)
#print(mp1.actions(testState))
node = Node(mp1.initial)
#print(node.path_cost+round(math.dist(node.state, mp1.goal),2))

f1=A_StarSearchAgentProgram(math.dist)
#f1(mp1)
Astar_PacManAgent1=ProblemSolvingMazeAgentAstar(initState,mazeWorldGraph2,goalState)
testNode = (0,0)
#Astar_PacManAgent1.program(mp1)
#Astar_PacManAgent1(testNode)

PacmanWorld1=MazeNavigationEnvironment(mazeWorldGraph2)

Astar_PacManAgent2=ProblemSolvingMazeAgentAstar(initState,mazeWorldGraph2,goalState)
mp2=MazeProblem(initState,goalState,mazeWorldGraph2)
#Astar_PacManAgent2.program(mp2)

print(initState,goalState)
intTupleTostr(goalState)

enemies = []
for i in range(len(maze1)):
    for j in range(len(maze1[0])):
        if maze1[i][j] == 3:
            enemies.append(Ghost((i,j)))
for i in enemies:
    PacmanWorld1.add_thing(i)
food = []
for i in range(len(maze1)):
    for j in range(len(maze1[0])):
        if maze1[i][j] == 2:
            food.append(FoodPellet((i,j)))
for i in food:
    PacmanWorld1.add_thing(i)

nodeColors.setdefault('goal', "green")
nodeColors.setdefault('init', "gold")
for node in net_maze.nodes:
    if node['id']==intTupleTostr(goalState):
        node['color']=nodeColors['goal']
    elif node['id']==intTupleTostr(initState):
        node['color']=nodeColors['init']
#Graph with goal highlighted
#net_maze.show("PacmanWorld1.html", notebook=False)

Astar_PacManAgent3=ProblemSolvingMazeAgentAstarMANHAT(initState,mazeWorldGraph2,goalState)
print(f"Agent performance: {Astar_PacManAgent3.performance}")
PacmanWorld1.add_thing(Astar_PacManAgent3)
PacmanWorld1.run()
