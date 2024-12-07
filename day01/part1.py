list1 = []
list2 = []
with open("input.txt") as file:
	for line in file:
		elems = line.split()
		list1.append(int(elems[0]))
		list2.append(int(elems[1]))

list1.sort()
list2.sort()

res = 0

for i in range(len(list1)):
	res += abs(list1[i] - list2[i])

print(res)