# Import dependencies
import streamlit as st
import streamlit.components.v1 as components #to display the HTML code
#from st_image_button import st_image_button

import networkx as nx #Networkx for creating graph data
from pyvis.network import Network #to create the graph as an interactive html object


from src.CSPclass import CSP, CSPBasic
from src.algorithms import backtracking_search

nodeColors={
    "empty":"white",
    "filled": "yellow"
}





def main():
    if "clicked" not in st.session_state:
        st.session_state["clicked"] = False
        
    tab1, tab2 = st.tabs(["Initial Sudoku", "Graph of constraints"])
    
    
    sudokuNeighbors,sudokuDomains,sudokuConstraints1=getSudokuData()        
    basicSudokuCSP=CSP(variables=sudokuNeighbors.keys(),neighbors=sudokuNeighbors, domains=sudokuDomains, constraints=sudokuConstraints1)
    #basicSudokuCSP=CSPBasic(variables=sudokuNeighbors.keys(),neighbors=sudokuNeighbors, domains=sudokuDomains, constraints=sudokuConstraints1)
    backtrack = False
    
    if not st.session_state["clicked"]:        
        if st.button("Run Backtrack"):
            print("button pressed")
            st.session_state["clicked"]=True
            result = backtracking_search(basicSudokuCSP)
            print(result)
            backtrack=True
            
            
        
    
    with tab1:
        st.header("Pre-Backtrack Asterisk Sudoku")
        
        # Define the number of rows you want
        num_rows = 9
        # Define the number of columns per row
        columns_per_row = 9
        vars=list(basicSudokuCSP.variables)
        #print("test1 "+str(vars))
        buildGraph(basicSudokuCSP, nodeColors)
        #print(basicSudokuCSP.domains)
        basicSudokuCSP.support_pruning()
        #print(basicSudokuCSP.curr_domains)
        

            
        
    with tab2:
        
        buildGraph(basicSudokuCSP, nodeColors)
        
        if backtrack:
            st.success("Backtrack applied. Check new domains")
            buildGraph(basicSudokuCSP, nodeColors, backtrack)
            #print(basicSudokuCSP.curr_domains)
 
            
        
        #st.button("Run AC-3", on_click= , args= [option])
        
         

        
def getSudokuData():
    import sudokuData
    var1=sudokuData.ROWS
    var2=sudokuData.COLUMNS
    filled=sudokuData.FILLED

    vars=set()

    for letter in var1:
        for number in var2:
            vars.add(letter+str(number))
    
    sudokuNeighbors={}
    for letter in var1:
        for number in var2:
            sudokuNeighbors[letter+str(number)]=[]
            
    for key1 in sudokuNeighbors.keys():
        for key2 in sudokuNeighbors.keys():
            ##this is creating duplicates for those in the same row/column and square
            if key1 != key2:
                if key1[1] == key2[1]:
                    sudokuNeighbors[key1].append(key2)
                elif key1[0] == key2[0]:
                    sudokuNeighbors[key1].append(key2)
                for i in sudokuData.GROUPS:
                    if key1 in i and key2 in i and key2 not in sudokuNeighbors[key1]:
                        sudokuNeighbors[key1].append(key2)

            
    sudokuDomains={var:[filled[var]] if var in filled else [ch for ch in range(1,10)] for var in sudokuNeighbors.keys()}
    sudokuConstraints1 = lambda X, x, Y, y: x!=y
    
    return sudokuNeighbors,sudokuDomains,sudokuConstraints1

        
        
        
def buildGraph(SudokuCSP, nodeColors, backtrack=False):
    netSudoku= Network(
                bgcolor ="#242020",
                font_color = "white",
                height = "750px",
                width = "100%"
                ) 
    
    nodeColorsDict={}
    nodeTitlesDict={}
    nodeLabelsDict={}
    nodes=list(SudokuCSP.variables)
    #print(backtrack)
    #print(SudokuCSP.curr_domains)

    for node in nodes:
        #print("in node for")
        if len(SudokuCSP.domains[node])==1:
            nodeColorsDict.setdefault(node,nodeColors["filled"])
            if backtrack:
                print("in if")
                nodeTitlesDict.setdefault(node,str(SudokuCSP.curr_domains[node][0]))
            else:
                nodeTitlesDict.setdefault(node,str(SudokuCSP.domains[node][0]))
            nodeLabelsDict.setdefault(node,str(SudokuCSP.domains[node][0]))           
        else:
            nodeColorsDict.setdefault(node,nodeColors["empty"])
            if backtrack:
                print("in else")
                string_list = [str(i) for i in SudokuCSP.curr_domains[node]]
               
            else:
                string_list = [str(i) for i in SudokuCSP.domains[node]]
            nodeTitlesDict.setdefault(node, ",".join(string_list) )
                
            nodeLabelsDict.setdefault(node,"")      
           
            
    x_coords = {}
    y_coords = {}

    for node in nodes:
        if node[0].lower()=="a":
            y_coords.setdefault(node,50)            
        elif node[0].lower()=="b":
            y_coords.setdefault(node,100)
        elif node[0].lower()=="c":
            y_coords.setdefault(node,150)
        elif node[0].lower()=="d":
            y_coords.setdefault(node,200)
        elif node[0].lower()=="e":
            y_coords.setdefault(node,250)
        elif node[0].lower()=="f":
            y_coords.setdefault(node,300)
        elif node[0].lower()=="g":
            y_coords.setdefault(node,350)
        elif node[0].lower()=="h":
            y_coords.setdefault(node,400)
        elif node[0].lower()=="i":
            y_coords.setdefault(node,450)
        x_coords.setdefault(node,int(node[1])*50)
           
            
    
    # initialize graph
    g = nx.Graph()
    
    # add the nodes
    for node in nodes:
        g.add_node(node, color=nodeColorsDict[node], size=10, title=nodeTitlesDict[node], label=nodeLabelsDict[node],  x=x_coords[node],y=y_coords[node])

    # add the edges
    #print("test2 "+str(SudokuCSP.neighbors))
    
    
    for nodeFrom in SudokuCSP.neighbors.keys():
        for nodeTo in SudokuCSP.neighbors[nodeFrom]:        
            if nodeFrom[0]==nodeTo[0]: # row const-s
                g.add_edge(nodeFrom,nodeTo, color="red")
            elif nodeFrom[1]==nodeTo[1]: # col const-s
                g.add_edge(nodeFrom,nodeTo, color="blue")
            else:
                g.add_edge(nodeFrom,nodeTo, color="green") # grouping con-s
            
    #print("test3 "+str(g.edges))
    # generate the graph
    netSudoku.from_nx(g)
    netSudoku.toggle_physics(False)
    #netSudoku.show("asteriskSudoku.html", notebook=False)
    
    netSudoku.save_graph('L7_AsteriskSudoku.html')
    HtmlFile = open(f'L7_AsteriskSudoku.html', 'r', encoding='utf-8')
    components.html(HtmlFile.read(), height = 1200,width=1000)
    

    
    
    
    
if __name__ == '__main__':
    main()
        