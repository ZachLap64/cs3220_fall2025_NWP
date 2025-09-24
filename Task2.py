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

for data in json_data['groups']:
  house=Dynasty.Dynasty(data['name'])
  for character in data['characters']:
    house.append(character)
  print(house)
  print("Our members:")
  for person in house:
    print(person)
  print(f"We have {house.getStrength()} family members!!!")

corpusData=json_data['groups']
GameOfThronesHouses=GameOfThronesGraph.GameOfThronesGraph(corpusData)
#print(GameOfThronesHouses.houses)

if "Stark" in GameOfThronesHouses:
    print("stark is here!!!")

visualisationData={}
legendData=[]
for house in GameOfThronesHouses:
  print(house)
  print(f"Strength: {house.getStrength()}")
  visualisationData[house.name]=house.getStrength()
  legendData.append(house.name)
print(visualisationData)
print(legendData)


# #Configure your x and y values from the dictionary:
# x= list(visualisationData.keys())
# y= list(visualisationData.values())

# #Create the graph = create seaborn barplot
# ax=sns.barplot(x=x,y=y)

# #specifyy axis labels
# ax.legend(legendData)
# sns.move_legend(ax, "upper left", bbox_to_anchor=(1.05, 1))
# ax.set(xlabel='Houses',
#        ylabel='Strength (N family members)',
#        title='Strength of GameOfThronesHouses')

# plt.xticks(rotation=45)
# #display barplot
# plt.show()


g = nx.Graph() # graph initialization

N_houses=0
colorKeys=[]
for house in GameOfThronesHouses:
    if house.name!="Include":
        N_houses+=1
        colorKeys.append(house.name)
sns.color_palette("husl", N_houses) # N_houses colors
#print(colorKeys)
nodeColors=dict(zip(colorKeys, [tuple(int(c*255) for c in cs) for cs in sns.color_palette("husl", N_houses)]))
#print(nodeColors)

for house in GameOfThronesHouses:
  if house.name!="Include":
    # add the house's name as a node to the graph g (houses's strength values is used as a node's size)
    g.add_node(house.name, size=house.getStrength())
    for character in house.characters:
      g.add_node(character)

for node, attributes in g.nodes(data=True): # run this code to check your code above
  print(f"Node: {node}, Attributes: {attributes}")

#-------------------------------------------
#Just characters and house names for edges
myEdges = []
for house in GameOfThronesHouses: #every house
  if house.name!="Include": #ignoring Include since its just a list of character not in houses
    tmp = [] #temp list for internal connections, resetting with each new house
    for person in house: #for each person in a house
      myEdges.append((person, house.name)) #add edge between person and their house
#-------------------------------------------
#-------------------------------------------
#Characters have edges with houses and edges with each other
# myEdges = []
# for house in GameOfThronesHouses: #every house
#   if house.name!="Include": #ignoring Include since its just a list of character not in houses
#     tmp = [] #temp list for internal connections, resetting with each new house
#     for person in house: #for each person in a house
#       myEdges.append((person, house.name)) #add edge between person and their house
#       tmp.append(person) #add person to tmp list
#       for ch in tmp: #we will make edge with person and everyone in the tmp list already
#         if ch != person: #no edges with yourself, not sure if required
#           myEdges.append((ch, person)) #add edge between person and house member in temp list
#-------------------------------------------

  #bad code I want to ask hannah about
      # for other in house: #for each person in the same house again
      #   if person != other: #don't make an edge with yourself
      #     if (person, other) not in myEdges: #if edge is not already present
      #       myEdges.append((person, other)) #add edge between person and another in the house



print("Connections between a House and its family members:") # run this code to check your code above
print(myEdges)

g.add_edges_from(myEdges) # run this code to add edges to our graph g
list(g.edges)# run this code  to check the edges in our graph g
print(len(list(g.edges))) # N of edges =89!!! check yours :)

GameOfThronesNet = Network(
                bgcolor ="#242020",
                font_color = "white",
                height = "1000px",
                width = "100%",
                notebook=True,
                cdn_resources = "remote")

# generate the graph
GameOfThronesNet.from_nx(g) 

for node in GameOfThronesNet.nodes:
    if node["id"] in GameOfThronesHouses:
        # Convert RGB to hexadecimal string
        node["color"] = '#%02x%02x%02x' % nodeColors[node["id"]]
    else:
        for house in GameOfThronesHouses: 
            if house.name !="Include":# apple the coloer of the House to this family member
                if node["id"] in house:
                    node["color"] = '#%02x%02x%02x' % nodeColors[house.name]

print(GameOfThronesNet.nodes)
GameOfThronesNet.show("GameOfThronesNet.html",notebook=False)