import streamlit as st
from src.environmentClass import Environment


class MazeEnvironment(Environment):
    def __init__(self, navGraph):
        super().__init__()
        self.status = navGraph

    def percept(self, agent):
        return agent.state
    
    def is_agent_alive(self, agent):
        return agent.alive
    
    def update_agent_alive(self, agent):
        if agent.performance <= 0:
            agent.alive = False
            print("Agent {} is dead.".format(agent))
        elif agent.state==agent.goal or len(agent.seq)==0:
            if agent.treasured:
                agent.alive = False
                if len(agent.seq)==0:
                    print("Agent reached all goals")
                else:
                    print(f"Agent reached the goal: {agent.goal}")
            else:
                agent.treasured = True
                agent.oldgoal = agent.goal
                agent.goal=["end"]
                agent.seq=(agent.search(agent.formulate_problem(agent.state,agent.goal)))

    def execute_action(self, agent, action):
        if self.is_agent_alive(agent):
            agent.state=agent.update_state(agent.state, action)
            agent.performance -= 1
            print(f"Agent in {agent.state} with performance = {agent.performance}")
            self.update_agent_alive(agent)

    def step(self):
        if not self.is_done():
            actions = []
            for agent in self.agents:
                #st.write(agent)
                if agent.alive:
                    action=agent.seq.pop(0)
                    print("Agent decided to do {}.".format(action))
                    actions.append(action)
                else:
                    actions.append("")
            for (agent, action) in zip(self.agents, actions):
                self.execute_action(agent, action)
        else:
            print("There is no one here who could work...")