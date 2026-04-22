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