import sys

def heuristic(grid, depth):
	for r in range(3):
		if grid[r][0] == "x" and grid[r][1] == "x" and grid[r][2] == "x":
			return sys.maxsize - depth
		if grid[r][0] == "o" and grid[r][1] == "o" and grid[r][2] == "o":
			return -sys.maxsize + depth

	for c in range(3):
		if grid[0][c] == "x" and grid[1][c] == "x" and grid[2][c] == "x":
			return sys.maxsize - depth
		if grid[0][c] == "o" and grid[1][c] == "o" and grid[2][c] == "o":
			return -sys.maxsize + depth

	if grid[0][0] == "x" and grid[1][1] == "x" and grid[2][2] == "x":
		return sys.maxsize - depth
	if grid[0][0] == "o" and grid[1][1] == "o" and grid[2][2] == "o":
		return -sys.maxsize + depth

	if grid[0][2] == "x" and grid[1][1] == "x" and grid[2][0] == "x":
		return sys.maxsize - depth
	if grid[0][2] == "o" and grid[1][1] == "o" and grid[2][0] == "o":
		return -sys.maxsize + depth

	return 0

def draw(grid):
	ans = True
	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if grid[r][c] == "":
				ans = False
				break
	return ans

def copy(grid):
	ans = []
	for r in grid:
		ans.append(r[:])

	return ans

def children(grid, a):
	ans = []

	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if grid[r][c] == "":
				grid[r][c] = a
				ans.append(copy(grid))
				grid[r][c] = ""

	return ans

def minimax(grid, player, depth):
	if heuristic(grid, depth) != 0:
		return heuristic(grid, depth)

	elif draw(grid):
		return 0

	if player == "max":
		ans = -sys.maxsize

		for child in children(grid, "x"):
			ans = max(ans, minimax(child, "min", depth + 1))

		return ans

	elif player == "min":
		ans = sys.maxsize

		for child in children(grid, "o"):
			ans = min(ans, minimax(child, "max", depth + 1))

		return ans

def print_grid(grid):
	for row in grid:
		print(row)
	print()


if __name__ == "__main__":
	grid = [
			["", "", ""],
			["", "", ""],
			["", "", ""]
			]

	# print("heuristic", heuristic(grid))
	# print("worst_case:", minimax(grid, "min"))

	depth = 0
	while heuristic(grid, depth) == 0:
		print("play:")

		invalid = True
		while invalid:
			rc = input().split(" ")
			row, col = int(rc[0]), int(rc[1])

			if row < len(grid) and col < len(grid[row]) and grid[row][col] == "":
				grid[row][col] = "x"
				depth += 1
				invalid = False

			if invalid: print("\nInvalid move!\n\nplay again:")

		print_grid(grid)


		if heuristic(grid, depth) > 0:
			print("VICTORY !!")
			break


		# print("worst_case:", minimax(grid, "min", depth))

		# for child in children(grid, "o"):
		# 	print("worst_case:", minimax(child, "max", 1))
		# 	print_grid(child)

		worst_case = sys.maxsize
		for child in children(grid, "o"):
			if minimax(child, "max", depth + 1) <= worst_case:
				worst_case = minimax(child, "max", depth + 1)
				grid = child
				# print(worst_case)
				# print_grid(grid)

		depth += 1		

		if heuristic(grid, 0) < 0:
			print("YOU LOSE !!")
			break

		if draw(grid):
			print("DRAW !!")
			break

		# print("***")

		print_grid(grid)