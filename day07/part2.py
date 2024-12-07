def test(cur_val, res, values, next):
	if cur_val == res and next == len(values):
		return True
	if cur_val > res:
		return False
	if next >= len(values):
		return False
	new_val = cur_val + values[next]
	if test(new_val, res, values, next + 1):
		return True
	new_val = cur_val * values[next]
	if test(new_val, res, values, next + 1):
		return True
	new_val = int(str(cur_val) + str(values[next]))
	if test(new_val, res, values, next + 1):
		return True
	return False

result = 0
with open("input.txt") as file:
	for line in file:
		res = int(line.split(":")[0])
		values = list(map(int, line.split(":")[1].split()))
		
		if test(values[0], res, values, 1):
			result += res

print(result)
