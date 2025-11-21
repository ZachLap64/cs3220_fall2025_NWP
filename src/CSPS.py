from src.CSPclass import CSP
from src.utils import *

def MapColoringCSP(colors, neighbors):
    """Make a CSP for the problem of coloring a map with different colors
    for any two adjacent regions. Arguments are a list of colors, and a
    dict of {region: [neighbor,...]} entries. This dict may also be
    specified as a string of the form defined by parse_neighbors."""
    if isinstance(neighbors, str):
        neighbors = parse_neighbors(neighbors)
    return CSP(list(neighbors.keys()), UniversalDict(colors), neighbors, different_values_constraint)


def not_next_to_constraint(seat1, val1, seat2, val2, csp, assignment={}):
    #Constraint: All assignments must be different, and B cannot sit next to A, C, or E.
    if assignment != {}:
        assigned_values = set()
        for var in csp.variables:
            if var in assignment:
                value = assignment[var]
                if value in assigned_values:
                    return False  # Duplicate value found
                assigned_values.add(value)
    if val1 == val2:
        return False
    if val1 == 'B' and (val2 == 'E' or val2 == 'A' or val2 == 'C'):
        return False
    if val2 == 'B' and (val1 == 'E' or val1 == 'A' or val1 == 'C'):
        return False
    return True

def TableCSP(guests, neighbors):

    if isinstance(neighbors, str):
        neighbors = parse_neighbors(neighbors)
    return CSP(list(neighbors.keys()), UniversalDict(guests), neighbors, not_next_to_constraint)

