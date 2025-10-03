from AgentCat import AgentCat
from CatFriendlyHouse import CatFriendlyHouse

a1 = AgentCat()
e1 = CatFriendlyHouse()
print("State of the Environment: {}".format(e1.status))
e1.add_thing(a1)
e1.run(5)