#!/usr/local/bin/python 

def dfs(node, start, visited=None):
	next = [start]
	if visited is None: visited = []

	while next:
		child = next.pop()
		if child not in visited:		# if not visited yet
			visited.append(child)
			if child in node:			# if adjecent node exist/edge
				next.extend(node[child])

	print(visited)

def bfs(node, start, visited=[]):
	next = [start]
	while next:
		child = next.pop(0)
		if child not in visited:		# if not visited yet
			visited.append(child)
			if child in node:			# if adjecent node exist/edge
				next.extend(node[child])

	print(visited)

if __name__ == '__main__':
	data = { 1 : [ 2, 3],
			 2 : [ 4, 5],
			 3 : [ 6] }
			 
	print(data)
	dfs(data, 1)			# avoid [] gotch
	bfs(data, 1)
	del data[1]
	bfs(data, 2, [])		# list ambiguity without []
