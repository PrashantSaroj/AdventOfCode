from collections import deque

def elevation(node):
    if node == 'S':
        return ord('a')
    if node == 'E':
        return ord('z')
    else:
        return ord(node)

def canJump(node1, node2):
    # can jump from node1 to node2
    return elevation(node2) - elevation(node1) <= 1

def neighbours(i, j, n, m, graph):
    adj = []
    if i - 1 >= 0 and canJump(graph[i][j], graph[i-1][j]):
        adj.append((i-1, j))
    if j - 1 >= 0 and canJump(graph[i][j], graph[i][j-1]):
        adj.append((i, j-1))
    if i + 1 < n and canJump(graph[i][j], graph[i+1][j]):
        adj.append((i+1, j))
    if j + 1 < m and canJump(graph[i][j], graph[i][j+1]):
        adj.append((i, j+1))
    return adj


def bfs(graph, start):
    n, m = len(graph), len(graph[0])
    dist = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    Q = deque()
    Q.append(start)

    while len(Q) > 0:
        i, j = Q.popleft()
        for neighbour in neighbours(i, j, n, m, graph):
            if not visited[neighbour[0]][neighbour[1]]:
                visited[neighbour[0]][neighbour[1]] = True
                dist[neighbour[0]][neighbour[1]] = dist[i][j] + 1
                Q.append(neighbour)
    
    return dist[20][107]


graph = list(map(list, open('in.txt', 'r').read().split('\n')))

allDistances = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 'a' or graph[i][j] == 'S':
            allDistances.append(bfs(graph, (i, j)))

print(sorted(allDistances))


