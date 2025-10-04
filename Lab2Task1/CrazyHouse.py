from src.environmentClass import Environment
from locations import roomA,roomB,roomC,roomD,roomE,rooms
from residents import *
import random

class CrazyHouse(Environment):
    def __init__(self):
        super().__init__()
        mk = random.randint(0,4)
        mkt = Milk()
        ms = random.randint(0,4)
        mst = Mouse()
        dg = random.randint(0,4)
        dgt = Dog()
        self.residents = [mkt,mst,dgt]
        self.status = {roomA:"empty", roomB:"empty", roomC:"empty", roomD:"empty", roomE:"empty"}
        if mk != ms:
            self.status[mk] = [mkt]
        if ms == dg:
            ms += random.choice([-1,1])
            self.status[ms] = mst
        else:
            self.status[ms] = mst
        if mk == dg:
            self.status[mk] = [mkt,dgt]
        else:
            self.status[dg] = [dgt]
        
        
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
                if agent.location != 4:
                    agent.location += 1
                agent.performance -= 1
                self.update_agent_alive(agent)
            if action == "MoveLeft":
                if agent.location != 0:
                    agent.location -= 1
                agent.performance -= 1
                self.update_agent_alive(agent)
            if action == "Eat":
                if isinstance(self.status[agent.location],Mouse):
                    if agent.performance >= 3:
                        agent.performance += 10
                        self.status[agent.location] = "empty"
                    else:
                        agent.performance -= 1
                        self.update_agent_alive(agent)
                else:
                    agent.performance -= 1
                    self.update_agent_alive(agent)
            if action == "Drink":
                if any(isinstance(a,Milk) for a in self.status[agent.location]):
                    agent.performance += 5
                    self.status[agent.location] = "empty"
                else:
                    agent.performance -=1
                    self.update_agent_alive(agent)
            if action == "Fight":
                if any(isinstance(a,Dog) for a in self.status[agent.location]):
                    if agent.performance >= 10:
                        agent.performance += 20
                        self.status[agent.location] = "empty"
                    else:
                        agent.performance -= 10
                        self.update_agent_alive(agent)
                else:
                    agent.performance -= 1
                    self.update_agent_alive(agent)


    def default_location(self,thing):
        print("Cat is starting in a random room...")
        return random.choice(rooms)
                










