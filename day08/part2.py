antennas = {}

width = 0
height = 0
with open("input.txt") as file:
	y = 0
	for line in file:
		x = 0
		for char in line.strip():
			if char != ".":
				if char not in antennas:
					antennas[char] = []
				antennas[char].append((x, y))
			x += 1
		width = x
		y += 1
	height = y

antinodes = set()
for _, value in antennas.items():
	for i in range(len(value)):
		for j in range(i + 1, len(value)):
			dx = value[i][0] - value[j][0]
			dy = value[i][1] - value[j][1]
			
			x = value[i][0] - dx
			y = value[i][1] - dy
			while 0 <= x < width and 0 <= y < height:
				antinodes.add((x, y))
				x -= dx
				y -= dy

			x = value[j][0] + dx
			y = value[j][1] + dy
			while 0 <= x < width and 0 <= y < height:
				antinodes.add((x, y))
				x += dx
				y += dy

print(len(antinodes))