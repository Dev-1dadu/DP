#dp8
def add_edge_bfs(graph, u, v):
	if u not in graph:
		graph[u] = []
	if v not in graph:
		graph[v] = []
	graph[u].append(v)
	graph[v].append(u)
def bfs(graph, start):
	visited=[]
	queue=[start]
	visited.append(start)
	print("\nGraph traversal starts from", start," :")
	while queue:
		node=queue.pop(0)
		print(node, end=" ")
		for neighbour in graph[node]:
			if neighbour not in visited:
				visited.append(neighbour)
				queue.append(neighbour)
def dfs(matrix, visited, node, names):
	visited[node]=True
	print(names[node],end=" ")
	for i in range(len(matrix)):
		if matrix[node][i]==1 and not visited[i]:
			dfs(matrix, visited, i, names)

n=int(input("Enter number of locations:"))
names=[]
for i in range(n):
	loc=input(f"Enter name of location {i+1} :")
	names.append(loc)
graph= {}
matrix = [[0]*n for _ in range(n)]

e=int(input("Enter no of routes:"))
print("Enter routes(e.g. A B ):")

for _ in range(e):
	u, v=input().split()
	add_edge_bfs(graph, u, v)
	u_index=names.index(u)
	v_index=names.index(v)
	matrix[u_index][v_index]=1
	matrix[v_index][u_index]=1
start=input("Enter starting location:")
bfs(graph, start)
visited=[False]*n
start_index=names.index(start)
print("\n DFS traversal starting from",start, ":")
dfs(matrix,visited,start_index,names)

		