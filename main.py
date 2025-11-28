import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
from pyvis.network import Network
from src.utils import parse_neighbors, schedule_constraints
from src.CSPclass import CSP
from src.algorithms import min_conflicts1


# neighbors1 = parse_neighbors('X: Y; Y: Z')
# domains1 = {'X': [4,5,6,7], 'Y': [4,5,6,8,9], 'Z':[3,5,6,7,9]}
# constraints1 = lambda X, x, Y, y: x==y

# print(neighbors1)

# #If variables is empty, it becomes domains.keys().
# CSP1=CSP(variables=None,neighbors=neighbors1, domains=domains1, constraints=constraints1)
# solution1=min_conflicts1(CSP1)

# print(solution1)

nodeColors={
    "empty":"white",
    "filled": "yellow"
}

def main():
    if "clicked" not in st.session_state:
        st.session_state["clicked"] = False

    # Variables
    variables = ['PPM_lec1', 'PPM_lec2', 'PPM_lab1', 'PPM_lab2',
                'ALG_lec1', 'ALG_lec2', 'ALG_lab1',
                'OS_lec1', 'OS_lec2', 'OS_lab1',
                'DB_lec1', 'DB_lec2', 'DB_lab1']

    # Domain: (day, slot) where day is 0-4 (Mon-Fri) and slot is 0-2 (class1-3)
    time_slots = [(day, slot) for day in range(5) for slot in range(3)]
    domains = {var: time_slots[:] for var in variables}

    # Neighbors: each variable is constrained with every other variable
    # This creates a complete graph since all variables must satisfy constraints with each other
    neighbor_string = '; '.join([f'{var}: {" ".join([v for v in variables if v != var])}'for var in variables])

    neighbors = parse_neighbors(neighbor_string)

    # print(neighbor_string)
    #print(variables)
    #print(neighbors['PPM_lec1'])

    classCSP = CSP(variables, domains, neighbors, schedule_constraints)

    minConflicts = False
    if not st.session_state["clicked"]:        
        if st.button("Run Min-Conflicts"):
            print("button pressed")
            st.session_state["clicked"]=True
            result = min_conflicts1(classCSP)
            #print(result)
            classCSP.result = result
            minConflicts=True

    st.header("Min-Conflicts Scheduling")
    buildGraph(classCSP, nodeColors)

    if minConflicts:
        st.success("Min-conflicts applied. Check new domains.")
        buildGraph(classCSP,nodeColors,minConflicts)

    #result = min_conflicts1(classCSP)
    #print(result)



def buildGraph(csp, nodeColors, minConflicts=False):
    netSchedule= Network(
                bgcolor ="#242020",
                font_color = "white",
                height = "750px",
                width = "100%"
                ) 
    
    nodeColorsDict={}
    nodeTitlesDict={}
    nodeLabelsDict={}
    nodes=list(csp.variables)

    for node in nodes:
        if len(csp.domains[node])==1:
            nodeColorsDict.setdefault(node,nodeColors["filled"])
            if minConflicts:
                nodeTitlesDict.setdefault(node,str(csp.result[node]))
            else:
                nodeTitlesDict.setdefault(node,str(csp.domains[node][0]))
            nodeLabelsDict.setdefault(node,str(csp.domains[node][0]))           
        else:
            nodeColorsDict.setdefault(node,nodeColors["empty"])
            if minConflicts:
                string_list = [str(csp.result[node])]
               
            else:
                string_list = [str(i) for i in csp.domains[node]]
            nodeTitlesDict.setdefault(node, ",".join(string_list) )
                
            nodeLabelsDict.setdefault(node,"") 

    x_coords = {}
    y_coords = {}

    if minConflicts:
        for node in nodes:
            print(csp.result[node])
            #print(csp.result[node][0])
            y_coords.setdefault(node,(int(csp.result[node][0])+1)*100)
            x_coords.setdefault(node,(int(csp.result[node][1])+1)*100)

    g = nx.Graph()

    for node in nodes:
        if minConflicts:
            g.add_node(node, color=nodeColorsDict[node], size=10, title=nodeTitlesDict[node], label=nodeLabelsDict[node],  x=x_coords[node],y=y_coords[node])
        else:
            g.add_node(node, color=nodeColorsDict[node], size=10, title=nodeTitlesDict[node], label=nodeLabelsDict[node])
    netSchedule.from_nx(g)
    netSchedule.toggle_physics(False)

    netSchedule.save_graph('L7_AsteriskSudoku.html')
    HtmlFile = open(f'L7_AsteriskSudoku.html', 'r', encoding='utf-8')
    components.html(HtmlFile.read(), height = 1200,width=1000)



if __name__ == "__main__":
    main()
