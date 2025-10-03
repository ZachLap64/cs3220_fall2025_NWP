from src.agentPrograms import RandomAgentProgram
from src.agentClass import Agent
import rules

def RandomCatAgent():
    return Agent(RandomAgentProgram(rules.actionList))