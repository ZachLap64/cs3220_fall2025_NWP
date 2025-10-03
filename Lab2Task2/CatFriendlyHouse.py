from src.environmentClass import Environment
from locations import room1,room2
import random, Milk, Sausage

class CatFriendlyHouse(Environment):
    def __init__(self):
        super().__init__()
        self.status = {room1:"empty",room2:"empty"}
        mk = random.randint(0,1)
        self.status[mk] = "MilkHere"
        self.status[1-mk] = "SausageHere"

    def percept(self, agent):
        return agent.location, self.status[agent.location]
    
    def is_agent_alive(self, agent):
        return agent.alive
    
    def update_agent_alive(self, agent):
        if agent.performance <= 0:
            agent.alive = False
            print("Agent {} is dead.".format(agent))

    def execute_action(self, agent, action):
        if self.is_agent_alive(agent):
            if action == "MoveRight":
                if agent.location == 0:
                    agent.location = 1
                agent.performance -= 1
            elif action == "MoveLeft":
                if agent.location == 1:
                    agent.location = 0
                agent.performance -= 1
            elif action == "Drink":
                if self.status[agent.location] == "MilkHere":
                    self.status[agent.location] = "empty"
                    mk = Milk.Milk()
                    agent.performance += mk.calories * mk.weight
                else:
                    agent.performance -= 1
            elif action == "Eat":
                if self.status[agent.location] == "SausageHere":
                    self.status[agent.location] = "empty"
                    sg = Sausage.Sausage()
                    agent.performance += sg.calories * sg.weight
                else:
                    agent.performance -= 1

    def default_location(self,thing):
        print("Cat is starting in a random room...")
        return random.choice([room1,room2])
