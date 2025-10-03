from src.agentClass import Agent
from src.agentPrograms import TableDrivenAgentProgram
from rules import table

def AgentCat():
     return Agent(TableDrivenAgentProgram(table))