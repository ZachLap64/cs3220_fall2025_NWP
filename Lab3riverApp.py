# Import dependencies
import streamlit as st
import streamlit.components.v1 as components #to display the HTML code

import networkx as nx #Networkx for creating graph data
from pyvis.network import Network #to create the graph as an interactive html object



from src.graphClass import Graph
from src.riverGraphClass import riverGraph
from data.riverData import riverWorld
from data.riverData import riverStatesLocations
from src.riverProblemClass import RiverProblem
from src.riverProblemSolvingAgentClass import RiverProblemSolvingAgent
from src.PS_agentPrograms import BestFirstSearchAgentProgram
from src.agents import ProblemSolvingRiverAgentBFS
from src.naigationEnvironmentClass import NavigationEnvironment

# from src.trivialVacuumEnvironmentClass import TrivialVacuumEnvironment
# from src.agents import RandomVacuumAgent


def drawBtn(e,a,c):
    option= [e,a,c]
    st.button("Run One Agent's Step", on_click= AgentStep, args= [option])
    
def AgentStep(opt):
    st.header("Resolving River Problem ...")
    e,a,c= opt[0],opt[1],opt[2]
    if not st.session_state["clicked"]:
        st.session_state["env"]=e
        st.session_state["agent"]=a
        st.session_state["nodeColors"]=c    
    
    if e.is_agent_alive(a):
        e.step()
        st.success(" Agent now at : {}.".format(a.state))
        st.info("Current Agent performance {}:".format(a.performance))
        c[a.state]="orange"
        st.info("State of the Environment:")
        buildGraph(e.status, c) 
    else:
        if a.state==a.goal:
            st.success(" Agent now at the goal state: {}.".format(a.state))
        else:
            st.error("Agent in location {} and it is dead.".format(a.state))
        
    st.session_state["clicked"] = True
        
    
        
def buildGraph(graphData, nodeColorsDict):
    net_RiverWorld = Network( heading="Lab3. River World Problem",
                bgcolor ="#242020",
                font_color = "white",
                height = "750px",
                width = "100%",
                directed = True, 
    ) # do this
    
    # initialize graph
    riverWorldGraph = riverGraph(riverWorld, riverStatesLocations())
    
    # add the nodes
    for node in riverWorldGraph.nodes():
        x,y=riverWorldGraph.getLocation(node)
        net_RiverWorld.add_node(node, x=x, y=y, color=nodeColorsDict[node])
    
    # add the edges
    edge_weights = {(k, v2) : k2 for k, v in riverWorld.items() for k2, v2 in v.items()}#actions
    edges=[]
    for node_source in riverWorldGraph.nodes():
        for node_target, actCost in riverWorldGraph.get(node_source).items():
        #action=riverWorld[node_source]
        #print(action)
            if (node_source,node_target) not in edges and (node_target, node_source):
                net_RiverWorld.add_edge(node_source, node_target, label=edge_weights[(node_source,node_target)])
                edges.append((node_source,node_target))              
    #riverWorldGraph.add_edges_from(edges)
    
    # generate the graph
    #net_RiverWorld.from_nx(riverWorldGraph)
    
    net_RiverWorld.save_graph('L3_RiverGraph.html')
    HtmlFile = open(f'L3_RiverGraph.html', 'r', encoding='utf-8')
    components.html(HtmlFile.read(), height = 1200,width=1000)
    
    
def makeDefaultColors(dictData):
    nodeColors=dict.fromkeys(dictData.keys(), "white")
    return nodeColors
        
    



def main():
    
        
    if "clicked" not in st.session_state:
        st.session_state["clicked"] = False
        
    if "env" not in st.session_state:
        st.session_state["env"]=None
        
    if "agent" not in st.session_state:
        st.session_state["agent"]=None
        
    if "nodeColors" not in st.session_state:
        st.session_state["nodeColors"]=None
        
    if not st.session_state["clicked"]:
        # Set header title
        st.header("Problem Solving Agents: River Crossing")
        st.header("_Initial Env._", divider=True)
        
        riverWorldGraph = riverGraph(riverWorld, riverStatesLocations())
        nodeColors=makeDefaultColors(riverWorldGraph.graph_dict)
        
        initState="LLLL"
        goalState="RRRR"
        
        rp1=RiverProblem(initState,goalState,riverWorldGraph)
        rpsa1=RiverProblemSolvingAgent(initState,riverWorldGraph,goalState)
        BFSagent1=ProblemSolvingRiverAgentBFS(initState,riverWorldGraph,goalState) 
                      
        st.header("State of the Environment", divider="red")
        nodeColors[rp1.state]="red"
        nodeColors[rp1.goal]="green"
        buildGraph(riverWorldGraph, nodeColors)
        st.info(f"The Agent in: {BFSagent1.state} with performance {BFSagent1.performance}.")
        st.info(f"The Agent goal is: {BFSagent1.goal} .")
                
        drawBtn(rp1,BFSagent1,nodeColors)
    
            
        
    if st.session_state["clicked"]:
        if st.session_state["env"].is_agent_alive(st.session_state["agent"]):
            #st.warning("Agent Step Done!")
            st.success(" Agent is working...")
            drawBtn(st.session_state["env"],st.session_state["agent"], st.session_state["nodeColors"])
       
    
    
    
        
        
        
                
            
    
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    

