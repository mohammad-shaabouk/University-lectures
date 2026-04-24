
# التمرين الثاني 

from collections import deque

# تعريف الشبكة
grid = [
    ['S', '.', '.', '#'],
    ['.', '#', '.', '.'],
    ['.', '.', '.', 'G']
]

rows = len(grid)
cols = len(grid[0])

# إيجاد نقطة البداية والهدف
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'S':
            start = (i, j)
        if grid[i][j] == 'G':
            goal = (i, j)

# اتجاهات الحركة
directions = [(-1,0), (1,0), (0,-1), (0,1)]

# BFS
queue = deque([start])
visited = set([start])
parent = {}   # لتتبع المسار
queue_order = []  # ترتيب الدخول إلى الطابور

while queue:
    current = queue.popleft()
    queue_order.append(current)

    if current == goal:
        break

    for d in directions:
        ni = current[0] + d[0]
        nj = current[1] + d[1]

        if rows > ni >= 0 and cols > nj >= 0:
            if grid[ni][nj] != '#' and (ni, nj) not in visited:
                queue.append((ni, nj))
                visited.add((ni, nj))
                parent[(ni, nj)] = current

# إعادة بناء المسار
path = []
node = goal
while node != start:
    path.append(node)
    node = parent[node]
path.append(start)
path.reverse()

# طباعة النتائج
print(":ترتيب دخول العقد إلى الطابور")
print(queue_order)

print("\n:المسار النهائي")
print(path)

print("\n:عدد الحركات")
print(len(path) - 1)

print("\n:(Parent لكل عقدة) شجرة البحث")
for child in parent:
    print(f"{parent[child]} -> {child}")

# التمرين الثالث
'''
from collections import deque
tree = {
  'S' : ['A','B'],
  'A' : ['C','D'],
  'B' : ['E','F'],
  'E' : ['G'],
  'C' : [],
  'D' : [],
  'F' : [],
  'G' : [],
}
nodes = []
def BFS(tree,start,goal):
  if goal not in tree:
    print("Goal Not Found")
    return
  q = deque([start])
  visited = set()
  while q:
    node = q.popleft()
    if node == goal:
      nodes.append(node)
      print("Found The Goal")
      print(nodes)
      return
    if node not in visited :
      visited.add(node)
      nodes.append(node)
      for neighbor in tree[node]:
        q.append(neighbor)
        print(f"Neighbor[{node}] is {tree[node]}")

BFS(tree,'S','G')
'''

    # التمرين الرابع

'''
graph = {
    'S':['A', 'B'],
    'A':['C', 'D'],
    'B':['D'],
    'D':['G'],
    'C':[],
    'G':[]
}
graph2 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
graph3 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}
graph4 = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': ['F'],
    'D': ['F'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}
def dfs(graph, start, goal):
    stack = [start]          # Stack
    visited = set()          # Visited nodes
    parent = {start: None}   # لتتبع المسار

    while stack:
        node = stack.pop()

        if node == goal:
            # بناء المسار
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in parent:
                    stack.append(neighbor)
                    parent[neighbor] = node

    return None


print(dfs(graph, 'S', 'G'))
print(dfs(graph2, 'A', 'D'))
print(dfs(graph3, 'A', 'C'))
print(dfs(graph3, 'A', 'D'))
print(dfs(graph4, 'S', 'G'))
print(dfs(graph, 'S', 'B'))

'''

# التمرين الخامس

'''
import heapq

def uniformcostsearch_list(graph, start, goal):
    if start == goal:
        return [start], [start], 0
    # الجبهة: heap من العناصر [cost, -counter, node, path]
    frontier = [(0, 0, start, [start])]
    visited = {}
    expansion_order = []
    counter = 1

    while frontier:
        # استخراج أقل كلفة باستخدام heapq
        cost, _, node, path = heapq.heappop(frontier)

        # تجاهل العقدة إذا سبق زيارتها بكلفة أفضل
        if node in visited and visited[node] <= cost:
            continue

        visited[node] = cost
        expansion_order.append(node)

        # التحقق من الوصول للهدف
        if node == goal:
            return expansion_order, path, cost

        # توسيع العقدة
        for neighbor, edge_cost in graph.get(node, []):
            newcost = cost + edge_cost
            heapq.heappush(frontier, (newcost, -counter, neighbor, path + [neighbor]))
            counter += 1

    return None, None, None

#تعريف الرسم البياني كما في التمرين الخامس
graph = {
    'S': [('A', 1), ('B', 1)],
    'A': [('C', 2), ('D', 5)],
    'B': [('E', 1)],
    'C': [('G', 3)],
    'E': [('G', 2)]
}

expansion, path, cost = uniformcostsearch_list(graph, 'S', 'G')

print("ترتيب التوسيع:  path.ipynb:46 - Uniform_Cost_Search.ipynb:46", expansion)
print("المسار:  path.ipynb:47 - Uniform_Cost_Search.ipynb:47", " → ".join(path))
print("الكلفة:  path.ipynb:48 - Uniform_Cost_Search.ipynb:48", cost)

'''

#⭐ ماذا يفعل هذا الكود؟

#1) يستخدم heapq بدل list
#python
#frontier = [(0, 0, start, [start])]
#heapq.heappop(frontier)
#  heapq يضمن استخراج العنصر بأقل كلفة بكفاءة أفضل

#2) نضيف -counter للترتيب الصحيح عند تساوي الكلفات
#python
#heapq.heappush(frontier, (newcost, -counter, neighbor, path + [neighbor]))
#  -counter يجعل الأحدث أولاً عند تساوي الكلفات (LIFO بدل FIFO)

#3) نوسّع العقدة ونضيف الأبناء للـ heap
#python
#heapq.heappush(frontier, (newcost, -counter, neighbor, path + [neighbor]))


#4) عند الوصول للهدف نرجع:
#- ترتيب التوسيع
#- المسار
#- الكلفة


#⭐ النتيجة الصحيحة:


#ترتيب التوسيع: ['S', 'A', 'C', 'B', 'E', 'G']
#المسار: S → A → C → G
#الكلفة: 6

