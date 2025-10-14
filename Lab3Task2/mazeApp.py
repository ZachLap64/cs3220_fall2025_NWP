import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
from pyvis.network import Network
from mazeWorldData import mazeActions, treasures, mazeData
from src.graphClass import Graph
from mazeEnvironment import MazeEnvironment
from mazeAgent import MazeAgent
from src.PS_agentPrograms import BestFirstSearchAgentProgram



def drawBtn(e,a,c):
    option= [e,a,c]
    st.button("Run One Agent's Step", on_click= AgentStep, args= [option])

def AgentStep(opt):
    st.header("Resolving Maze Navigation Problem ...")
    e,a,c= opt[0],opt[1],opt[2]
    if not st.session_state["clicked"]:
        st.session_state["env"]=e
        st.session_state["agent"]=a
        st.session_state["nodeColors"]=c    
    
    if e.is_agent_alive(a):
        e.step()
        st.success(" Agent now at : {}.".format(a.state))
        st.info("Current Agent performance {}:".format(a.performance))
        st.info(f"The Agent goal is: {a.goal} .")
        #st.write(a.state)
        for i in a.oldgoal:
            c[i] = "white"
        a.oldgoal = []
        c[a.state]="orange"
        for i in a.goal:
            c[i]="green"
        st.info("State of the Environment:")
        buildGraph(e.status, c) 
        drawBtn(e,a,c)
    else:
        if a.state in a.goal:
                st.success(" Agent now at the goal state: {}.".format(a.state))
        else:
            st.error("Agent in location {} and it is dead.".format(a.state))
        
    st.session_state["clicked"] = True

def buildGraph(graphData, nodeColorsDict):
    netMaze = Network(
                bgcolor ="#242020",
                font_color = "white",
                height = "750px",
                width = "100%") 
    
    nodes=graphData.nodes()
    g = nx.Graph()
    for node in nodes:
        g.add_node(node, color=nodeColorsDict[node])

    edges=[]
    for node_source in graphData.nodes():
        for node_target, dist in graphData.get(node_source).items():
            if set((node_source,node_target)) not in edges:
                edges.append(set((node_source,node_target)))  
    #st.write(edges)              
    g.add_edges_from(edges)
    #st.write(g.edges(data=True))

    netMaze.from_nx(g)
    netMaze.save_graph("L3_MazeGraph.html")
    HtmlFile = open(f'L3_MazeGraph.html', 'r', encoding='utf-8')
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
        st.header("Problem Solving Agents: Maze Navigation Problem")
        st.header("_Initial Env._", divider=True)
        mazeGraph = Graph(mazeData)
        #st.write("after graph made")
        nodeColors=makeDefaultColors(mazeGraph.graph_dict)
        initState = "start"
        goalStates = treasures
        #goalStates = ["end"]
        re=MazeEnvironment(mazeGraph)
        BFSMazeAgent = MazeAgent(initState,mazeGraph,goalStates,BestFirstSearchAgentProgram())
        #st.write("after agent made")
        BFSMazeAgent.seq=(BFSMazeAgent.search(BFSMazeAgent.formulate_problem(BFSMazeAgent.state,goalStates)))

        re.add_thing(BFSMazeAgent)
        #st.write("added thing")
        st.header("State of the Environment", divider="red")
        nodeColors[BFSMazeAgent.state]="red"
        #nodeColors[BFSMazeAgent.goal]="green"
        for i in BFSMazeAgent.goal:
            nodeColors[i]="green"
        #st.write(nodeColors)
        buildGraph(mazeGraph, nodeColors) 
        #st.write("after graph built")
        st.info(f"The Agent in: {BFSMazeAgent.state} with performance {BFSMazeAgent.performance}.")
        st.info(f"The Agent goal is: {BFSMazeAgent.goal} .")

        drawBtn(re,BFSMazeAgent,nodeColors)

        if st.session_state["clicked"]:
            if st.session_state["env"].is_agent_alive(st.session_state["agent"]):
                st.success(" Agent is working...")
                drawBtn(st.session_state["env"],st.session_state["agent"], st.session_state["nodeColors"])
       

        
if __name__ == '__main__':
    main()