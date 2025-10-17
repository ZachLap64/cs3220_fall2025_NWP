#How do we decide which node from the frontier to expand next?
from src.nodeClass import Node
from queue import PriorityQueue

nodeColors={
    "start":"red",
    "goal": "green",
    "frontier": "orange",
    "expanded":"pink"
}

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
  
 
def IDSearchAgentProgram(f=None):
  def program(problem):
    # maxDepth = 1000
    # for depth in range(maxDepth):
    #    result = depth_limited_search(problem, depth)
    #    if problem.goal_test(result):
    #     return result
    #def iterative_deepening_search(problem):
      depth = 0
      while True:
        result = depth_limited_search(problem, depth)
        if result != 'cutoff':
            return result
        depth += 1

  return program

def depth_limited_search(problem, limit):
      node = Node(problem.initial)
      print("start of recusion")
      return recursive_dls(node, problem, limit)

def recursive_dls(node, problem, limit):
      if problem.goal_test(node.state):
        return node.solution()
      elif node.depth == 0:
        print("returning cutoff")
        return 'cutoff'
      else:
        cutoff_occurred = False
        print("in recursion")
        for child in node.expand(problem):
            result = recursive_dls(child, problem, limit - 1)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result != 'failure':
                return result
        return 'cutoff' if cutoff_occurred else 'failure'

#def depth_limited_search(graph, current, goal, limit, path):
    # path.append(current)

    # if current == goal:
    #     return path

    # if limit <= 0:
    #     path.pop()
    #     return None

    # for neighbor in graph.get(current, []):
    #     if neighbor not in path:
    #         result = depth_limited_search(graph, neighbor, goal, limit - 1, path)
    #         if result is not None:
    #             return result

    # path.pop()
    # return None

# def iterative_deepening_search(graph, start, goal, max_depth=100):
#     for depth in range(max_depth):
#         path = []
#         print(f"Trying depth limit: {depth}")
#         result = depth_limited_search(graph, start, goal, depth, path)
#         if result is not None:
#             return result
#     return None

 
 




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