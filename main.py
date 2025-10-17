from src.asteroidData import *
from src.graphProblemClass import GraphProblem
from src.maze2025GraphClass import mazeGraph
from src.mazeProblemClass import MazeProblem
from src.PS_agentPrograms import BestFirstSearchAgentProgram
from src.agents import *
from pyvis.network import Network 
from src.naigationEnvironmentClass import MazeNavigationEnvironment

#--------------------------------------------------------
#Making the maze and the maze graph

n=7
maze1=makeMaze(n)
print(maze1)

mazeALLActs=defineMazeActions(maze1)
#print(mazeALLActs)

mazeAvalActs=defineMazeAvailableActions(maze1)
#print(mazeAvalActs)

maze1TM=makeMazeTransformationModel(mazeAvalActs)
#print(maze1TM)
#print(list(maze1TM.keys()))

mazeWorldGraph = mazeGraph(maze1TM, mazeStatesLocations(list(maze1TM.keys())))
#print(mazeWorldGraph.nodes())
#print(mazeWorldGraph.graph_dict)
#print(mazeWorldGraph.origin)
#print(mazeWorldGraph.locations)
#print(mazeWorldGraph.get((0, 1), (0,2)))

net_maze = Network( heading="Lab4. Examples of Maze World Problem",
                bgcolor ="#242020",
                font_color = "white",
                height = "750px",
                width = "100%" 
) # do this
nodeColors={
    "wall":"red",
    "path": "white"
}
nodeColorsList=[]
for node in mazeWorldGraph.origin.keys():
    if maze1[node[0],node[1]]==1:
        nodeColorsList.append(nodeColors["path"])
    else:
        nodeColorsList.append(nodeColors["wall"])
nodeColorsList
nodes=["-".join(str(item) for item in el) for el in mazeWorldGraph.origin.keys()]
#print(nodes)
x_coords = []
y_coords = []
for node in mazeWorldGraph.origin.keys():
    x,y=mazeWorldGraph.getLocation(node)
    x_coords.append(x)
    y_coords.append(y)
sizes=[10]*len(nodes)
#hidden labels, and hover titles
net_maze.add_nodes(nodes, color=nodeColorsList, x=x_coords, y=y_coords, size=sizes, title=nodes)
for node in net_maze.nodes:
    node['label']=''
#print(net_maze.nodes)
edge_weights = {(intTupleTostr(k), intTupleTostr(v2)) : k2 for k, v in mazeWorldGraph.origin.items() for k2, v2 in v.items()}#actions
#print(edge_weights)
edges=[]
for node_source in mazeWorldGraph.nodes():
    for node_target, action in mazeWorldGraph.get(node_source).items():
        #node_target or node_source is a tuple -> convert to str
        if (intTupleTostr(node_source),intTupleTostr(node_target)) not in edges and (intTupleTostr(node_target), intTupleTostr(node_source)):
            net_maze.add_edge(intTupleTostr(node_source),intTupleTostr(node_target), label=edge_weights[(intTupleTostr(node_source),intTupleTostr(node_target))])
            edges.append((intTupleTostr(node_source),intTupleTostr(node_target)))
# Disable physics
net_maze.toggle_physics(False)
#SHOW GRAPH VISUALIZATION
#net_maze.show("graph1.html", notebook=False)


#--------------------------------------------------------
#Maze environment and agent stuff

initState, goalState=(0,1),(4,3)
testState=(0,2)
mp1=MazeProblem(initState,goalState,mazeWorldGraph)
#print(mp1.actions(testState))

BFS_MazeAgent1=ProblemSolvingMazeAgentBFS(initState,mazeWorldGraph,goalState)
#print(BFS_MazeAgent1.goal)
testNode = (0,2)
#BFS_MazeAgent1(testNode)

#environment setup
maze_Env1=MazeNavigationEnvironment(mazeWorldGraph)
maze_Env1.status.graph_dict
#agent setup
BFS_MazeAgent2=ProblemSolvingMazeAgentBFS(initState,mazeWorldGraph,goalState)
print(BFS_MazeAgent2.performance)
print(initState,goalState)
intTupleTostr(goalState)
iDLS_agent = ProblemSolvingMazeAgentIDLS(initState,mazeWorldGraph,goalState)
print(iDLS_agent.performance)



#adjusting colours
nodeColors.setdefault('goal', "green")
nodeColors.setdefault('init', "gold")
for node in net_maze.nodes:
    if node['id']==intTupleTostr(goalState):
        node['color']=nodeColors['goal']
    elif node['id']==intTupleTostr(initState):
        node['color']=nodeColors['init']
#GRAPH VISUALIZATION
#net_maze.show("graphMaze1.html", notebook=False)

maze_Env1.add_thing(BFS_MazeAgent2)
maze_Env1.add_thing(iDLS_agent)
#maze_Env1.step()
maze_Env1.run()