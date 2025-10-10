import networkx as nx
from pyvis.network import Network
from mazeWorldData import *
from src.graphClass import Graph
from mazeEnvironment import MazeEnvironment
from mazeAgent import MazeAgent

netMaze = Network(heading="Task2. Navigating a maze of treasures",
                    bgcolor = "#242020",
                    font_color = "white",
                    height = "1000px",
                    width = "100%",
                    directed = True,
                    cdn_resources = "remote")

nodes = []
for i in len(maze):
    for j in len(maze[i]):
        if maze[i][j] != 0:
            nodes.append()