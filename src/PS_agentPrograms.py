#How do we decide which node from the frontier to expand next?
from src.nodeClass import Node
from queue import PriorityQueue

import math

nodeColors={
    "start":"red",
    "goal": "green",
    "frontier": "orange",
    "expanded":"pink"
}


def A_StarSearchAgentProgram(f=None):
  
    #f=math.dist
    
    def program(problem):
      print("Hi")

      node = Node(problem.initial)
 
      frontier = PriorityQueue()
      h=node.path_cost+round(math.dist(node.state, problem.goal),3)
      frontier.put((h,node))
      reached = {problem.initial:node}

      counter = 0

      while frontier:
        print(frontier.queue)
        node = frontier.get()[1]
        print("The node {} is extracted from frontier:".format(node.state))

        if problem.goal_test(node.state):
          print("We have found our goal: {}".format (node.state))
          print(f"Number of child nodes expanded {counter}")
          return node

        #reached.add(node.state)
        for child in node.expand(problem):
            if child.state not in reached or child.path_cost<reached[child.state].path_cost:
                #print(child)
                print("The child node {}.".format(child))
                h=child.path_cost+round(f(child.state, problem.goal),3)
                frontier.put((h,child))
                counter=counter+1
                reached.update({child.state:child})
            
      return None

    return program


def A_StarSearchAgentProgramMANHAT(f=None):
  
    #f=math.dist
    
    def program(problem):
      print("Hi")

      node = Node(problem.initial)
 
      frontier = PriorityQueue()
      h=node.path_cost+abs(node.state[0]-problem.goal[0])+abs(node.state[1]-problem.goal[1])
      frontier.put((h,node))
      reached = {problem.initial:node}

      counter = 0

      while frontier:
        print(frontier.queue)
        node = frontier.get()[1]
        print("The node {} is extracted from frontier:".format(node.state))

        if problem.goal_test(node.state):
          print("We have found our goal: {}".format (node.state))
          print(f"Number of child nodes expanded {counter}")
          return node

        #reached.add(node.state)
        for child in node.expand(problem):
            if child.state not in reached or child.path_cost<reached[child.state].path_cost:
                #print(child)
                print("The child node {}.".format(child))
                h=child.path_cost+abs(child.state[0]-problem.goal[0])+abs(child.state[1]-problem.goal[1])
                frontier.put((h,child))
                counter=counter+1
                reached.update({child.state:child})
            
      return None

    return program



def BestFirstSearchAgentProgram(f=None):
  #with BFS we choose a node, n, with minimum value of some evaluation function, f (n).
    
    def program(problem):

      node = Node(problem.initial)
      #node.color=nodeColors["start"]
      #print(node.state)
      frontier = PriorityQueue()
      frontier.put((1,node))
      print(f"The {node} is being pushed to frontier ...")
      #node.color=nodeColors["frontier"]
      reached = {problem.initial:node}

      while frontier:
        node = frontier.get()[1]
        #node.color=nodeColors["expanded"]
        print(f"The {node} is being extracted from frontier ...")

        if problem.goal_test(node.state):
          node.color=nodeColors["goal"]
          print(f"We have found our goal:  {node}!")
          return node

        #reached.add(node.state)
        for child in node.expand(problem):
            if child.state not in reached or child.path_cost<reached[child.state].path_cost:
                frontier.put((1,child))
                print(f"The child {child} is being pushed to frontier ...")
                #child.color=nodeColors["frontier"]
                reached.update({child.state:child})
            
        #node.color=nodeColors["expanded"]
      return None

    return program
  
 
def IDAStarSearchAgentProgram(f=None):
  def program(problem):
      
      max_depth = 10000
      root = Node(problem.initial)
      #print(type(root))
      #node = Node(problem.initial)
      fLimit = abs(root.state[0]-problem.goal[0])+abs(root.state[1]-problem.goal[1])
      #print(type(fLimit))
      reached = {problem.initial:root}
      for depth_limit in range(max_depth + 1):
        solution, fLimit = DFS_Contour(root, fLimit, problem, reached)
        #print(root)
        #print(type(solution))
        #print(type(fLimit))
        if solution is not None:
            #print(f"Goal found at depth: {depth_limit}")
            return solution
      print("Goal not found.")
      return None

  return program


def DFS_Contour(node, fLimit, problem, reached):
    nextfLimit = 10000
    print(node.state)
    print(f"Path cost {node.path_cost}")
    fCost = node.path_cost + abs(node.state[0]-problem.goal[0])+abs(node.state[1]-problem.goal[1])
    if fCost > fLimit:
        return None, fCost
    #if node == Node(problem.goal):
    #if problem.goal_test(node.state):
    if node.state == problem.goal:
        return node, fLimit
    #print(node)
    for child in node.expand(problem):
        if child.state not in reached or child.path_cost<reached[child.state].path_cost:
          reached.update({child.state:child})
          solution, newfLimit = DFS_Contour(child, fLimit, problem, reached)
          #print(result)
          if solution is not None:
            return solution, fLimit
          nextfLimit = min(nextfLimit, newfLimit)
    return None, nextfLimit
    
 
      











def BestFirstSearchAgentProgramForShow(f=None):
  #with BFS we choose a node, n, with minimum value of some evaluation function, f (n).
    
    def program(problem):
      #print(111)
      steps = 0
      allNodeColors = []
      nodeColors = {k : 'white' for k in problem.graph.nodes()}

      node = Node(problem.initial)
      nodeColors[node.state] = "yellow"
      steps += 1
      allNodeColors.append(dict(nodeColors))

      #print(node.state)
      frontier = PriorityQueue()
      frontier.put((1,node))

      nodeColors[node.state] = "orange"
      steps += 1
      allNodeColors.append(dict(nodeColors))



      reached = {problem.initial:node}

      while frontier:
        node = frontier.get()[1]
        nodeColors[node.state] = "red"
        steps += 1
        allNodeColors.append(dict(nodeColors))
        #print(node)

        if problem.goal_test(node.state):
          nodeColors[node.state] = "green"
          steps += 1
          allNodeColors.append(dict(nodeColors))
          return (node,steps,allNodeColors)
          

        #reached.add(node.state)
        for child in node.expand(problem):
            if child.state not in reached or child.path_cost<reached[child.state].path_cost:
                frontier.put((1,child))
                nodeColors[child.state] = "orange"
                steps += 1
                allNodeColors.append(dict(nodeColors))

                reached.update({child.state:child})

        # modify the color of explored nodes to blue
        nodeColors[node.state] = "blue"
        steps += 1
        allNodeColors.append(dict(nodeColors))
            
      return None

    return program