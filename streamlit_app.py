import pandas as pd
from pyvis.network import Network
import streamlit as st
import streamlit.components.v1 as components

data = pd.read_csv("data/game-of-thrones-battles.csv")
#print(data.head())

battles_df = data.loc[:,['name','attacker_king','defender_king','attacker_size','defender_size']]
#print(battles_df.head())
#print(battles_df.info())

battles_df_cleaned = battles_df.dropna()
#print(battles_df_cleaned.head())
#print(battles_df_cleaned.info())

#print(f"Attacking Kings: {battles_df_cleaned.attacker_king.unique()}")
#print(f"Defending Kings: {battles_df_cleaned.defender_king.unique()}")

net5kings = Network(heading="Task1. Building Interactive Network of battles of the War of 5",
                    bgcolor = "#242020",
                    font_color = "white",
                    height = "1000px",
                    width = "100%",
                    directed = True,
                    cdn_resources = "remote")

Akings = battles_df_cleaned.attacker_king.unique()
Dkings = battles_df_cleaned.defender_king.unique()
KingNodes = set(Akings.flatten()).union(set(Dkings.flatten()))


for i in KingNodes:
    net5kings.add_node(i,value=1)
#net5kings.add_nodes(KingNodes)
#print(net5kings.nodes)

## get the start->end of the edges
potentialEdges = list(zip(battles_df_cleaned.attacker_king,battles_df_cleaned.defender_king))
#print(potentialEdges)
realEdges = list(set(potentialEdges))
#print(realEdges)

## get the weights of the edges
df = pd.DataFrame(potentialEdges)
count = (df.groupby([0,1]).size())
#print(count)

## get the names of the edges ready
tmpTitles = list(zip(battles_df_cleaned.attacker_king,battles_df_cleaned.defender_king,battles_df_cleaned.name))
dft = pd.DataFrame(tmpTitles)
tIndexes = (dft.groupby([0,1]).groups)
tEdges = []
for i in tIndexes:
    lst = []
    tmp = (dft.take(tIndexes[i]))
    lst += tmp.get(2).to_list()
    stri = ", ".join(lst)
    tEdges.append(stri)
#print(tEdges)

## add the edges to net5kings
for i in range(realEdges.__len__()):
    fr = realEdges[i][0]
    to = realEdges[i][1]
    #wght = count.iloc[i]
    for j in range(len(count)):
        if count.index[j][0] == fr:
            if count.index[j][1] == to:
                wght = count.iloc[j]
                ttl = tEdges[j]
                break
    #ttl = tEdges[i]
    #print("from: " + fr + ", to: " + to + ", weight: "+ str(wght) + ", \nbattles: ")
    #print(ttl)
    net5kings.add_edge(fr,to, value=int(wght), title=ttl)
#print(net5kings.edges)

## set the values and colours of the nodes
nodeColors = {0:'blue',1:'green',2:'orange',3:'purple',4:'gold',5:'red'}
tmp = net5kings.get_adj_list()
cnt = 0
for i in tmp:
    val = len(tmp[i])+1
    node = net5kings.get_node(i)
    node['value'] = val
    node['color'] = nodeColors[val]

#print(net5kings.nodes)
   
#net5kings.show("Lab1-task1.html", notebook=False)

htmlFile = open(f'Lab1-task1-net5kings.html', 'r', encoding='utf-8')
components.html(htmlFile.read(), height = 1200,width=1000)





