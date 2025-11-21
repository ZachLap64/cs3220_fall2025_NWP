from src.CSPclass import CSPBasic
from src.CSPclass import CSP
from src.utils import UniversalDict
from src.utils import different_values_constraint
from src.utils import parse_neighbors
from src.utils import *
from src.CSPS import *
from src.algorithms import *
from pyvis.network import Network


table="1: 2 6; 2: 3; 3: 4; 4: 5; 5: 6"
parse_neighbors(table)

tableCSP = TableCSP(list('ABCDE'), table)

print(tableCSP.domains)
print(tableCSP.variables)
print(tableCSP.neighbors)

domains = tableCSP.domains
variables = tableCSP.variables
neighbours = tableCSP.neighbors

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
for node in variables:
    net.add_node(node, label=node, title=f"Seat: {node}")

# Add edges
for node, nbrs in neighbours.items():
    for nbr in nbrs:
        net.add_edge(node, nbr)

# Save and open in browser
# net.show("graph_with_domains.html", notebook=False)
# BEFORE AC3 ****


AC3(tableCSP)

for var in tableCSP.variables:
    print(var, tableCSP.curr_domains[var])

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
for node, dom in tableCSP.curr_domains.items():
    net2.add_node(node, label=node, title=f"Domain: {dom}")

# Add edges
for node, nbrs in tableCSP.neighbors.items():
    for nbr in nbrs:
        net2.add_edge(node, nbr)

# Save and open in browser
# net2.show("graph_with_domains2.html", notebook=False)
# AFTER AC3 ****


result = backtracking_search(tableCSP)
print(result)

# Create a PyVis network
#net = Network(height="600px", width="100%", directed=False, notebook=False)
net3 = Network( heading="Lab7. Scheduling After Backtracking",
                bgcolor ="#242020",
                font_color = "white",
                height = "750px",
                width = "100%",
                directed = True, 
) # do this

# Add nodes with domain info as tooltips
for node, dom in result.items():
    net3.add_node(node, label=node, title=f"Guest: {dom}")

# Add edges
for node, nbrs in tableCSP.neighbors.items():
    for nbr in nbrs:
        net3.add_edge(node, nbr)

# Save and open in browser
net3.show("graph_with_domains3.html", notebook=False)
# AFTER BACKTRACKING ****




# australiaColors=UniversalDict(list('RGB'))
# australia="SA: WA NT Q NSW V; NT: WA Q; NSW: Q V; T: "
# parse_neighbors(australia)
# australiaCSP = MapColoringCSP(list('RGB'), australia)
# result = backtracking_search(australiaCSP)
# print(result)
