# Import dependencies
import streamlit as st
import streamlit.components.v1 as components #to display the HTML code
import pandas as pd
import networkx as nx #Networkx for creating graph data
import json
import io
import os
import Dynasty
import GameOfThronesGraph
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import seaborn as sns
from pyvis.network import Network
from pyvis.network import Network #to create the graph as an interactive html object


def data_load():
    file_name = "data/game-of-thrones-characters-groups.json"
    path="data"
    json_files = [os.path.join(root, name) 
              for root, dirs, files in os.walk(path) 
              for name in files 
              if name.endswith((".json"))] #If we needed to read several files extensions: if name.endswith((".ext1", ".ext2"))
    print('Number of JSON files ready to be loaded: ' + str(len(json_files)))
    print('Path to the first file: '+json_files[0])
    #Open the file using the name of the json file witn open() function
    #Read the json file using load() and put the json data into a variable.
    with open(json_files[0]) as f:
        json_data = json.load(f)
        #print(json_data)
        #print(json_data.keys)
    return json_data


def buildGraph(GameOfThronesHouses):
    GameOfThronesNet = Network(
                bgcolor ="#242020",
                font_color = "white",
                height = "1000px",
                width = "100%",
                notebook=True,
                cdn_resources = "remote")
    
    g = nx.Graph() # graph initialization

    N_houses=0
    colorKeys=[]
    for house in GameOfThronesHouses:
        if house.name!="Include":
            N_houses+=1
            colorKeys.append(house.name)
    sns.color_palette("husl", N_houses) # N_houses colors
    nodeColors=dict(zip(colorKeys, [tuple(int(c*255) for c in cs) for cs in sns.color_palette("husl", N_houses)]))

    for house in GameOfThronesHouses:
        if house.name!="Include":
        # add the house's name as a node to the graph g (houses's strength values is used as a node's size)
            g.add_node(house.name, size=house.getStrength())
            for character in house.characters:
                g.add_node(character)
    
    #Just characters and house names for edges
    myEdges = []
    for house in GameOfThronesHouses: #every house
        if house.name!="Include": #ignoring Include since its just a list of character not in houses
            for person in house: #for each person in a house
                myEdges.append((person, house.name)) #add edge between person and their house
    
    g.add_edges_from(myEdges) # run this code to add edges to our graph g

    #Generate the graph
    GameOfThronesNet.from_nx(g)
    #Set colors
    for node in GameOfThronesNet.nodes:
        if node["id"] in GameOfThronesHouses:
            # Convert RGB to hexadecimal string
            node["color"] = '#%02x%02x%02x' % nodeColors[node["id"]]
        else:
            for house in GameOfThronesHouses: 
                if house.name !="Include":# apple the coloer of the House to this family member
                    if node["id"] in house:
                        node["color"] = '#%02x%02x%02x' % nodeColors[house.name]
    
    HtmlFile = open(f'GameOfThronesNet.html', 'r', encoding='utf-8')
    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height = 1200,width=1000)
    
    

def main():
    json_data = data_load()
    corpusData=json_data['groups']
    GameOfThronesHouses=GameOfThronesGraph.GameOfThronesGraph(corpusData)


    tab1, tab2, tab3 = st.tabs([
    "Game of Thrones Houses", 
    "Members of Houses", 
    "Graph for Game of Thrones Houses"
    ])

    with tab1:
        st.header("Game of Thrones Houses")
        visualisationData={}
        legendData=[]
        for house in GameOfThronesHouses:
            st.print(house)
            st.print(f"Strength: {house.getStrength()}")
            visualisationData[house.name]=house.getStrength()
            legendData.append(house.name)

        #Configure your x and y values from the dictionary:
        x= list(visualisationData.keys())
        y= list(visualisationData.values())

        #Create the graph = create seaborn barplot
        ax=sns.barplot(x=x,y=y)

        #specifyy axis labels
        ax.legend(legendData)
        sns.move_legend(ax, "upper left", bbox_to_anchor=(1.05, 1))
        ax.set(xlabel='Houses',
        ylabel='Strength (N family members)',
        title='Strength of GameOfThronesHouses')

        plt.xticks(rotation=45)
        #display barplot
        #plt.show()
        st.pyplot(plt)

    with tab2:
        st.header("Members of Houses")
        for data in json_data['groups']:
            house=Dynasty.Dynasty(data['name'])
            for character in data['characters']:
                house.append(character)
            st.print(house)
            st.print("Our members:")
            for person in house:
                st.print(person)
            st.print(f"We have {house.getStrength()} family members!!!")

    with tab3:
        st.header("Graph for Game of Thrones Houses")
        buildGraph(GameOfThronesHouses)

        
       
if __name__ == '__main__':
    main()