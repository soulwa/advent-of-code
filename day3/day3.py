def trees_encountered(treemap, run, rise):
	idx = 0
	tree_count = 0
	for i in range(0, len(treemap), rise):
		if idx == 0:
			idx += run
			continue
		else:
			row = treemap[i]
			if row[idx % len(row)] == '#':
				tree_count += 1
				#print("pos {} ({}) in {}: {}".format(idx, idx % 11, row, row[idx % 11]))
				#print("pos {} ({}) in {}: {}".format(idx, idx % 11, row, row[idx % 11]))
			idx += run
	return tree_count


with open('input', 'r') as f:
	lines = [line for line in f]
	treemap = [row.strip() for row in lines]

	print("right 1, down 1: {}".format(trees_encountered(treemap, 1, 1)))
	print("right 3, down 1: {}".format(trees_encountered(treemap, 3, 1)))
	print("right 5, down 1: {}".format(trees_encountered(treemap, 5, 1)))
	print("right 7, down 1: {}".format(trees_encountered(treemap, 7, 1)))
	print("right 1, down 2: {}".format(trees_encountered(treemap, 1, 2)))
	print(trees_encountered(treemap, 1, 1) * trees_encountered(treemap, 3, 1) * trees_encountered(treemap, 5, 1) * 
		trees_encountered(treemap, 7, 1) * trees_encountered(treemap, 1, 2))

