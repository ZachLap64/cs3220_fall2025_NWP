from src.environmentClass import Environment
import math


class MazeNavigationEnvironment(Environment):
  def __init__(self, navGraph):
    super().__init__()
    self.status = navGraph
    self.ghosts = []
    self.food = []
    

  def percept(self, agent):
    #Returns the agent's location, and the location status (Dirty/Clean).
    return agent.state

  def is_agent_alive(self, agent):
    return agent.alive

  def update_agent_alive(self, agent):
    if agent.performance <= 0:
      agent.alive = False
      print("Agent {} is dead.".format(agent))
    elif agent.state==agent.goal or len(agent.seq)==0:
      agent.alive = False
      if len(agent.seq)==0:
        print("Agent reached all goals")
      else:
        print(f"Agent reached the goal: {agent.goal}")
      

  def execute_action(self, agent, action):
    '''Check if agent alive, if so, execute action'''
    if self.is_agent_alive(agent):
        """Change agent's location -> agent's state;
        Track performance.
        -1 for each move."""
        agent.state=agent.update_state(agent.state, action)
        agent.performance -= 1
        if agent.state == "down":
          agent.location = (agent.location[0]+1,agent.location[1])
        elif agent.state == "right":
          agent.location = (agent.location[0],agent.location[1]+1)
        elif agent.state == "down":
          agent.location = (agent.location[0]-1,agent.location[1])
        elif agent.state == "left":
          agent.location = (agent.location[0],agent.location[1]-1)
        print(f"Agent in {agent.state} with performance = {agent.performance}")
        for i in self.ghosts:
          if agent.location == i.location:
            print("Agent ran into a ghost!")
            if agent.performance > agent.strongThresh:
              print("Agent beat the ghost!")
              agent.performance = math.floor(agent.performance*0.9)
            else:
              print("Agent was beaten by the ghost!")
              agent.performance=0
        if self.food != None:
          for i in self.food:
            if agent.location == i.location:
              print("Agent ate a food pellet!")
              agent.performance *= 2
              self.food.remove(i)
        self.update_agent_alive(agent)

        # if action == 'Right':
        #     agent.location = loc_B
        #     agent.performance -= 1
        #     self.update_agent_alive(agent)
        # elif action == 'Left':
        #     agent.location = loc_A
        #     agent.performance -= 1
        #     self.update_agent_alive(agent)
        # elif action == 'Suck':
        #     if self.status[agent.location] == 'Dirty':
        #         agent.performance += 10
        #     self.status[agent.location] = 'Clean'

  # def default_location(self, thing):
  #       """Agents start in either location at random."""
  #       print("Agent is starting in random location...")
  #       return random.choice([loc_A, loc_B])
  
  def step(self):
    if not self.is_done():
        actions = []
        for agent in self.agents:
          if agent.alive:
            #with agent.state because for PS Agent we don't need to percive
            action=agent.seq.pop(0)
            print("Agent decided to do {}.".format(action))
            actions.append(action)
          else:
            actions.append("")
            
        for (agent, action) in zip(self.agents, actions):
          self.execute_action(agent, action)
    else:
        print("There is no one here who could work...")
  
  def add_thing(self, thing, location=None):
    #from agentClass import Agent
    from src.problemSolvingAgentProgramClass import SimpleProblemSolvingAgentProgram
    from src.ghostClass import Ghost
    from src.foodPelletClass import FoodPellet
    if thing in self.agents:
      print("Can't add the same agent twice")
    else:
      if isinstance(thing, SimpleProblemSolvingAgentProgram):
        thing(thing.state)
        thing.performance = 33
        #thing.location = location if location is not None else self.default_location(thing)
        print(f"The Agent in {thing.state} with performance {thing.performance}")
        self.agents.append(thing)
      elif isinstance(thing, Ghost):
        self.ghosts.append(thing)
      elif isinstance(thing, FoodPellet):
        self.food.append(thing)