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
			antinode1 = (value[i][0] + dx, value[i][1] + dy)
			antinode2 = (value[j][0] - dx, value[j][1] - dy)
			if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
				antinodes.add(antinode1)
			if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
				antinodes.add(antinode2)

print(len(antinodes))