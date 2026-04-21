#node = "A";
#moveCost = 15;
#visit = True;
#print(f"node name is {node} \n Move cost is {moveCost} \n visited ? {visit}");

#node = input("Enter Your node : ");
#goal = input("Enter Your goal : ");
#if node == goal :
#  print ("You arraived to your goal");
#else: 
#  print("Error");


#nodes = ["A","B","C","D","E"];
#for node in nodes :
#  print(f"The Node is {node}");

'''
empty = []
empty.append("A")
empty.append("B")
empty.append("C")
print(empty)
empty.pop()
print(empty)

'''

'''
# dict
graph = {
  "A":["B","C"],
  "B":["D"],
  "C":["E"],
  "D":[],
  "E":[],
}
print(graph.values())

'''

#for neighbor in graph["A"]:
#  print(neighbor);

#nodes = []
#visited = set()
#visited.add("A")
#if "A" in visited : 
#  print("the node is visited . ")


#def check_goal(node,goal):
#  if node == goal:
#    return True
#  return False
#print(check_goal("B","B"))

'''
from collections import deque
queue = deque()
queue.append("A")
queue.append("B")
queue.append("C")
print(queue)
queue.popleft()

'''

'''

from collections import deque
graph = {
  "S":["A","B"],
  "A":["C","D"],
  "B":["E"],
  "C":[],
  "D":["G"],
  "E":[],
  "G":[]
}
def bfs(graph,start,goal):
  queue = deque([start])
  visited = set()
  while queue:
    node = queue.popleft()
    if node == goal:
      print("Goal foundded . ")
      return
    if node not in visited :
      visited.add(node)
      for neighbor in graph[node]:
        queue.append(neighbor)
bfs(graph,"S","G")

'''