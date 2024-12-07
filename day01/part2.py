from collections import Counter

list1 = []
list2 = []
with open("input.txt") as file:
	for line in file:
		elems = line.split()
		list1.append(int(elems[0]))
		list2.append(int(elems[1]))

list2Counter = Counter(list2)

res = 0

for i in range(len(list1)):
	res += list1[i] * list2Counter[list1[i]]

print(res)