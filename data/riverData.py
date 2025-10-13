import random

riverWorldStates=['Left','Right']
agentLocations=['Left','Right']
agentActions=['boat','takeWolf','takeGoat','takeCabbage']

# Wolf, Goat, Cabbage, Farmer
#LLLL START
#LLLR BAD
#LLRL
#LLRR BAD
#LRLL 
#LRLR 
#LRRL BAD
#LRRR 
#RLLL 
#RLLR BAD
#RLRL 
#RLRR 
#RRLL BAD
#RRLR 
#RRRL BAD
#RRRR GOAL


LLLL=''.join(map(lambda x: x[0],(riverWorldStates[0],riverWorldStates[0], riverWorldStates[0], agentLocations[0])))
LLLR=''.join(map(lambda x: x[0],(riverWorldStates[0],riverWorldStates[0], riverWorldStates[0], agentLocations[1])))
LLRL=''.join(map(lambda x: x[0],(riverWorldStates[0],riverWorldStates[0], riverWorldStates[1], agentLocations[0])))
LLRR=''.join(map(lambda x: x[0],(riverWorldStates[0],riverWorldStates[0], riverWorldStates[1], agentLocations[1])))
LRLL=''.join(map(lambda x: x[0],(riverWorldStates[0],riverWorldStates[1], riverWorldStates[0], agentLocations[0])))
LRLR=''.join(map(lambda x: x[0],(riverWorldStates[0],riverWorldStates[1], riverWorldStates[0], agentLocations[1])))
LRRL=''.join(map(lambda x: x[0],(riverWorldStates[0],riverWorldStates[1], riverWorldStates[1], agentLocations[0])))
LRRR=''.join(map(lambda x: x[0],(riverWorldStates[0],riverWorldStates[1], riverWorldStates[1], agentLocations[1])))
RLLL=''.join(map(lambda x: x[0],(riverWorldStates[1],riverWorldStates[0], riverWorldStates[0], agentLocations[0])))
RLLR=''.join(map(lambda x: x[0],(riverWorldStates[1],riverWorldStates[0], riverWorldStates[0], agentLocations[1])))
RLRL=''.join(map(lambda x: x[0],(riverWorldStates[1],riverWorldStates[0], riverWorldStates[1], agentLocations[0])))
RLRR=''.join(map(lambda x: x[0],(riverWorldStates[1],riverWorldStates[0], riverWorldStates[1], agentLocations[1])))
RRLL=''.join(map(lambda x: x[0],(riverWorldStates[1],riverWorldStates[1], riverWorldStates[0], agentLocations[0])))
RRLR=''.join(map(lambda x: x[0],(riverWorldStates[1],riverWorldStates[1], riverWorldStates[0], agentLocations[1])))
RRRL=''.join(map(lambda x: x[0],(riverWorldStates[1],riverWorldStates[1], riverWorldStates[1], agentLocations[0])))
RRRR=''.join(map(lambda x: x[0],(riverWorldStates[1],riverWorldStates[1], riverWorldStates[1], agentLocations[1])))


riverWorld = (dict(
    LLLL=dict(boat=LLLR, takeWolf=RLLR, takeGoat=LRLR, takeCabbage=LLRR),
    LLLR=dict(boat=LLLL, takeWolf=LLLR, takeGoat=LLLR, takeCabbage=LLLR),
    LLRL=dict(boat=LLRR, takeWolf=RLRR, takeGoat=LRRR, takeCabbage=LLRL),
    LLRR=dict(boat=LLRL, takeWolf=LLRR, takeGoat=LLRR, takeCabbage=LLLL),
    LRLL=dict(boat=LRLR, takeWolf=RRLR, takeGoat=LRLL, takeCabbage=LRRR),
    LRLR=dict(boat=LRLL, takeWolf=LRLR, takeGoat=LLLL, takeCabbage=LRLR),
    LRRL=dict(boat=LRRR, takeWolf=RRRR, takeGoat=LRRL, takeCabbage=LRRL),
    LRRR=dict(boat=LRRL, takeWolf=LRRR, takeGoat=LLRL, takeCabbage=LRLL),
    RLLL=dict(boat=RLLR, takeWolf=RLLL, takeGoat=RRLR, takeCabbage=RLRR),
    RLLR=dict(boat=RLLL, takeWolf=LLLL, takeGoat=RLLR, takeCabbage=RLLR),
    RLRL=dict(boat=RLRR, takeWolf=RLRL, takeGoat=RRRR, takeCabbage=RLRL),
    RLRR=dict(boat=RLRL, takeWolf=LLRL, takeGoat=RLRR, takeCabbage=RLLL),
    RRLL=dict(boat=RRLR, takeWolf=RRLL, takeGoat=RRLL, takeCabbage=RRRR),
    RRLR=dict(boat=RRLL, takeWolf=LRLL, takeGoat=RLLL, takeCabbage=RRLR),
    RRRL=dict(boat=RRRR, takeWolf=RRRL, takeGoat=RRRL, takeCabbage=RRRL),
    RRRR=dict(boat=RRRL, takeWolf=LRRL, takeGoat=RLRL, takeCabbage=RRLL)
))


keyList = [
    LLLL,
    LLLR,
    LLRL,
    LLRR,
    LRLL,
    LRLR, 
    LRRL,
    LRRR,
    RLLL, 
    RLLR,
    RLRL, 
    RLRR, 
    RRLL,
    RRLR, 
    RRRL,
    RRRR
]


# def makeData():
#   d1 = {}
#   for i in range(len(keyList)):
#     d1[keyList[i]]=results[i]
#   return d1



def riverStatesLocations():
  x = []
  y = []
  n=len(keyList)
  for _ in range(n):
    x.append(random.randint(0, n+1)+100)
    y.append(random.randint(0, n+1)+100)
  zipped = zip(x, y)
  return dict(zip(keyList, zipped))



def getAction(dict):
  edge_weights = {(k, v2) : k2 for k, v in dict.items() for k2, v2 in v.items()}#actions
  return edge_weights
