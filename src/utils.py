from collections import defaultdict, Counter
import random


class UniversalDict:
    """A universal dict maps any key to the same value. 
    We use it here as the domains dict for CSPs 
    in which all variables have the same domain.
    >>> d = UniversalDict(list('RGB'))
    >>> d['SA']
    ['R','G','B']
    """

    def __init__(self, value): 
      self.value = value

    def __getitem__(self, key): 
      return self.value

    def __repr__(self): 
      return f'Any from {self.value}'


def different_values_constraint(A, a, B, b):
    """A constraint saying two neighboring variables must differ in value."""
    return a != b



def parse_neighbors(neighbors):
    """Convert a string of the form 'X: Y Z; Y: Z' into a dict mapping
    regions to neighbors. The syntax is a region name followed by a ':'
    followed by zero or more region names, followed by ';', repeated for
    each region name. If you say 'X: Y' you don't need 'Y: X'.
    >>> parse_neighbors('X: Y Z; Y: Z') == {'Y': ['X', 'Z'], 'X': ['Y', 'Z'], 'Z': ['X', 'Y']}
    True
    """
    dic = defaultdict(list)
    specs = [spec.split(':') for spec in neighbors.split(';')]
    for (A, Aneighbors) in specs:
        #print(A)
        A = A.strip()
        for B in Aneighbors.split():
            dic[A].append(B)
            dic[B].append(A)
    return dic


def count(seq):
    """Count the number of items in sequence that are interpreted as true."""
    return sum(map(bool, seq))

def first(iterable, default=None):
    """Return the first element of an iterable; or default."""
    return next(iter(iterable), default)





def min_conflicts_value1(csp, var, current):
    """Return the value that will give var the least number of conflicts.
    If there is a tie, choose at random."""
    print(f"var {var} (val, nConflicts):")
    varConflicts=[(val,csp.nconflicts(var, val, current)) for val in csp.domains[var]]
    print(f"{varConflicts}")
    return argmin_random_tie(csp.domains[var], key=lambda val: csp.nconflicts(var, val, current))

def argmin_random_tie(seq, key):
    """Return a minimum element of seq; break ties at random."""
    minElem=min(shuffled(seq), key=key)
    print(f"The value {minElem} -> selected")
    return minElem

def shuffled(iterable):
    """Randomly shuffle a copy of iterable."""
    items = list(iterable)
    random.shuffle(items)
    return items

# Constraint function
def schedule_constraints(X, x, Y, y):
    """
    X, Y: variable names (strings)
    x, y: values (day, slot) tuples
    Returns True if assignment is valid, False otherwise
    """
    day_x, slot_x = x
    day_y, slot_y = y
    
    # Constraint 1: No two sessions at same time slot
    if x == y:
        return False
    
    # Extract course name and type (lec/lab) from variable names
    course_x = X.rsplit('_', 1)[0]  # e.g., 'PPM' from 'PPM_lec1'
    type_x = X.rsplit('_', 1)[1][:3]  # e.g., 'lec' from 'PPM_lec1'
    
    course_y = Y.rsplit('_', 1)[0]
    type_y = Y.rsplit('_', 1)[1][:3]
    
    # Only apply course-specific constraints if same course
    if course_x == course_y:
        # Constraint 2: Two lectures from same course can't be on same day
        if type_x == 'lec' and type_y == 'lec' and day_x == day_y:
            return False
        
        # Constraint 3: Two lectures from same course can't be on adjacent days
        if type_x == 'lec' and type_y == 'lec' and abs(day_x - day_y) == 1:
            return False
        
        # Constraint 4: Two labs from same course can't be on adjacent days
        if type_x == 'lab' and type_y == 'lab' and abs(day_x - day_y) == 1:
            return False

        # Constraint 5: (Optional) Two labs from same course can't be on same day
        #if type_x == 'lab' and type_y == 'lab' and day_x == day_y:
        #    return False
        
    return True
