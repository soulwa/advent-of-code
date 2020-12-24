import itertools as it

numbers = dict()
pair_sums = dict()

with open("input", 'r') as f:
	for line in f:
		num = int(line)
		if 2020 - num in numbers:
			print(num * numbers[2020 - num])
		else:
			numbers[num] = num

with open("input", 'r') as f:
	nums = [int(i) for i in f]
	pairs = list(it.product(nums, nums))
	for p in pairs:
		pair_sums[p[0] + p[1]] = p
	for num in nums:
		if 2020 - num in pair_sums:
			pair = pair_sums[2020 - num]
			print(num * pair[0] * pair[1])
			break
		else:
			continue
