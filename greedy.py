import math
import heapq
import sys

def dist(graph, a, b):
	a_x = float(graph[a][2])
	a_y = float(graph[a][3])
	b_x = float(graph[b][2])
	b_y = float(graph[b][3])
	return math.sqrt((b_x - a_x)**2 + (b_y - a_y)**2)


def reconstruct_path(came_from, curr, start):
	ans = [curr]

	while curr != start:
		curr = came_from[curr]
		ans.append(curr)

	ans = list(reversed(ans))

	return ans


def a_star(graph, start_name, goal_name):
	for i in range(len(graph)):
		if graph[i][1] == start_name:
			start = i
			break

	goal = 1
	for i in range(len(graph)):
		if graph[i][1] == goal_name:
			goal = i
			break

	closed_set = set()
	open_set = set([start])

	came_from = {}

	g_score = {}
	g_score[start] = 0
	f_score = {}
	f_score[start] = dist(graph, start, goal)

	curr = start
	while len(open_set) > 0:
		for e in open_set:
			curr = e
			break

		for e in open_set:
			if f_score[e] < f_score[curr]:
				curr = e

		print(curr, graph[curr][1])
		if curr == goal:
			return reconstruct_path(came_from, curr, start), g_score[goal]

		open_set.remove(curr)
		closed_set.add(curr)

		neighbors = []
		if curr == 1:
			neighbors = [2, 3]
		elif curr % 2 == 0:
			if curr - 2 > 0: neighbors.append(curr - 2)
			if curr + 2 < len(graph): neighbors.append(curr + 2)
			neighbors.append(curr-1)
		elif curr % 2 == 1:
			neighbors.append(curr - 2)
			if curr + 2 < len(graph): neighbors.append(curr + 2)
			if curr + 1 < len(graph): neighbors.append(curr + 1)

		for n in neighbors:
			if n <= 0 or n >= len(graph):
				continue
			if n in closed_set: continue

			d = g_score[curr]
			h = dist(graph, n, goal)
			g = d + dist(graph, curr, n)

			if n not in open_set: open_set.add(n)
			elif n in g_score and g >= g_score[n]: continue

			came_from[n] = curr
			g_score[n] = g
			# f_score[n] = g_score[n] + h
			f_score[n] = h


if __name__ == "__main__":
	graph = []

	with open('input.txt') as file:
		for f in file:
			line = f[:-1].split(",")
			graph.append(line)

	graph = graph[:-1]
	# for line in graph:
	# 	print(line)

	start_name = 'Alice Springs'
	goal_name = 'Yulara'

	print(a_star(graph, start_name, goal_name))