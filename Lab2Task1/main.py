from agent import RandomCatAgent
from CrazyHouse import CrazyHouse

a1 = RandomCatAgent()
e1 = CrazyHouse()
print("State of the Environment: {}".format(e1.status))
e1.add_thing(a1)
a1.performance = 5
#print("RandomCatAgent is located at {}".format(a1.location))
e1.run()