from functools import cache

bags = dict()

@cache
def bag_search(key):
	val = bags[key][0]
	if 'shiny gold' in val:
		return 1
	elif val == []:
		return 0
	else:
		l = set([bag_search(bag) for bag in val]) # binary or
		if l == {0}:
			return 0
		else:
			return 1


@cache
def bag_count(key):
	val = bags[key]
	if val[0] == []:
		return 0
	else:
		return sum(val[1]) + sum([n * bag_count(k) for k, n in zip(val[0], val[1])])


with open('input', 'r') as f:
	count = 0
	for line in f:
		entry = line.split(' bags contain ')
		contained = entry[1].strip().split(', ')
		if contained[0][0] == 'n':
			num_bags = []
		else:
			num_bags = [int(s[0]) for s in contained]
		contained = [s[2:].rsplit(' bag')[0] for s in contained]
		if contained[0] == ' other':
			bags[entry[0]] = ([], num_bags)
		else:
			bags[entry[0]] = (contained, num_bags)
	for key in bags:
		count += bag_search(key)
	print(count)
	print(bag_count('shiny gold'))

