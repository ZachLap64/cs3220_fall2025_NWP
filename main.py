from data.riverData import riverWorld
from src.riverGraphClass import riverGraph
from data.riverData import riverStatesLocations
from pyvis.network import Network 
from src.riverProblemClass import RiverProblem
from src.riverProblemSolvingAgentClass import RiverProblemSolvingAgent
from src.PS_agentPrograms import BestFirstSearchAgentProgram
from src.agents import ProblemSolvingRiverAgentBFS

# print(riverWorld)
riverWorldGraph = riverGraph(riverWorld, riverStatesLocations())
# print(riverWorldGraph.graph_dict)
# print(riverWorldGraph.origin)

# print(riverWorldGraph.get(("LRLR")))
# print(riverWorldGraph.getLocation(("LRLR")))

net_RiverWorld = Network( heading="Lab3. River World Problem",
                bgcolor ="#242020",
                font_color = "white",
                height = "750px",
                width = "100%",
                directed = True, 
) # do this

#print(riverWorldGraph.nodes())
#net_VacuumWorld.add_nodes(vacuumWorldGraph.nodes())

for node in riverWorldGraph.nodes():
    x,y=riverWorldGraph.getLocation(node)
    net_RiverWorld.add_node(node, x=x, y=y)
# print(riverWorldGraph.get(("LRLR")))
# print(riverWorld)

edge_weights = {(k, v2) : k2 for k, v in riverWorld.items() for k2, v2 in v.items()}#actions
#print(edge_weights)

#print(len(edge_weights))

edges=[]
for node_source in riverWorldGraph.nodes():
    for node_target, actCost in riverWorldGraph.get(node_source).items():
        #action=vacuumWorld[node_source]
        #print(action)
        if (node_source,node_target) not in edges and (node_target, node_source):
            #net_VacuumWorld.add_edge(node_source,node_target, label=str(action))
            net_RiverWorld.add_edge(node_source,node_target, label=edge_weights[(node_source,node_target)])
            edges.append((node_source,node_target))

#net_RiverWorld.show("graph2.html", notebook=False)
initState = "LLLL"
goalState = "RRRR"
# print(initState)
# print(goalState)

rp1=RiverProblem(initState,goalState,riverWorldGraph)
#print(riverWorldGraph.graph_dict)
#print(rp1.actions("LLRL"))
#print(rp1.result("LLRL", 'boat'),rp1.result("LLRL", 'takeWolf'),rp1.result("LLRL", 'takeGoat'),rp1.result("LLRL", 'takeCabbage'))
cost=0
#rp1.path_cost(cost, "DCR", 'Suck',"DCR")
#print(initState, goalState)
rpsa1=RiverProblemSolvingAgent(initState,riverWorldGraph,goalState)
#print(rpsa1.formulate_problem(rpsa1.state,rpsa1.goal).actions("LLRL"))
BFSAP1=BestFirstSearchAgentProgram()
#print(rp1.initial)
seq=BFSAP1(rp1)
#print(seq)


BFSagent1=ProblemSolvingRiverAgentBFS(initState,riverWorldGraph,goalState)
#print(BFSagent1.seq) # no solution at the very begining
BFSagent1("LLLL") # the  __call__ method with the percept as a parameter
BFSagent1("RRRR")
BFSagent2=ProblemSolvingRiverAgentBFS("LLLL",riverWorldGraph,goalState)
BFSagent2("LRLR")