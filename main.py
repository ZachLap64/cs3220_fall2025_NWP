from src.CSPS import *
from src.algorithms import *
from src.utils import *
from pyvis.network import Network

# vars=list("A","B","C","D","E","F","G")
vars = ['A','B','C','D','E','F','G']
# neighbours = "A: B C; B: A C D; C: A B E F; D: B E; E: D C; F: C G; G: F"
n = "A: B C; B: C D; C: E F; D: E; E: ; F: G; G: "

neighbours = parse_neighbors(n)

domains = {
    'A': ['Mon','Tues','Wed'],
    'B': ['Tues'],
    'C': ['Mon','Tues','Wed'],
    'D': ['Mon','Tues','Wed'],
    'E': ['Mon','Tues','Wed'],
    'F': ['Wed'],
    'G': ['Mon','Tues','Wed'],
}

# print(vars)
# print(neighbours)
# print(domains)

scheduleCSP = SchedulingCSP(domains, neighbours)

print(scheduleCSP.variables)
print(scheduleCSP.neighbors)
print(scheduleCSP.domains)

constraints = lambda X, x, Y, y: x!=y




# Create a PyVis network
#net = Network(height="600px", width="100%", directed=False, notebook=False)
net = Network( heading="Lab6. Scheduling Pre AC3",
                bgcolor ="#242020",
                font_color = "white",
                height = "750px",
                width = "100%",
                directed = True, 
) # do this

# Add nodes with domain info as tooltips
for node, dom in domains.items():
    net.add_node(node, label=node, title=f"Domain: {dom}")

# Add edges
for node, nbrs in neighbours.items():
    for nbr in nbrs:
        net.add_edge(node, nbr)

# Save and open in browser
net.show("graph_with_domains.html", notebook=False)


AC3(scheduleCSP)

for var in scheduleCSP.variables:
    print(var, scheduleCSP.curr_domains[var])

# Create a PyVis network
#net = Network(height="600px", width="100%", directed=False, notebook=False)
net2 = Network( heading="Lab6. Scheduling After AC3",
                bgcolor ="#242020",
                font_color = "white",
                height = "750px",
                width = "100%",
                directed = True, 
) # do this

# Add nodes with domain info as tooltips
for node, dom in scheduleCSP.curr_domains.items():
    net2.add_node(node, label=node, title=f"Domain: {dom}")

# Add edges
for node, nbrs in scheduleCSP.neighbors.items():
    for nbr in nbrs:
        net2.add_edge(node, nbr)

# Save and open in browser
net2.show("graph_with_domains2.html", notebook=False)
