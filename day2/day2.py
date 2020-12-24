count = 0
count2 = 0

with open("input", 'r') as f:
	for line in f:
		line = line.split()
		bounds = line[0].split('-')
		lower = int(bounds[0])
		upper = int(bounds[1])
		constraint = line[1][0]
		if lower <= len(list(filter(lambda x: x == constraint, line[2]))) <= upper:
			count += 1
		else:
			continue

print(count)

with open("input", 'r') as f:
	for line in f:
		line = line.split()
		posns = line[0].split('-')
		lo = int(posns[0]) - 1
		hi = int(posns[1]) - 1
		constraint = line[1][0]
		if (line[2][lo] == constraint) ^ (line[2][hi] == constraint):
			count2 += 1
		else:
			continue

print(count2)