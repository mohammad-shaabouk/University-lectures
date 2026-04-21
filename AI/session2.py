#BFS

'''
from collections import deque

graph = {'S':['A','B'],'A':['C','D'],'B':['E','F'],'E':['G'],'C':[] , 'D':[],'F':[]}

nodes = []
def bfs(graph, start, goal):

    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        if node == goal:
            nodes.append(node)
            print("Done Founded")
            print(nodes)
            return
        if node not in visited:
            visited.add(node)
            nodes.append(node)
            for neighbor in graph[node]:
                queue.append(neighbor)

bfs(graph, "S", "G")


'''

