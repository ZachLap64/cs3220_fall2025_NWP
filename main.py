from src.utils import parse_neighbors
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
print(variables)
print(neighbors)
