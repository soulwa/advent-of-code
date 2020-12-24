import string

with open('input', 'r') as f:
	data = f.read().split('\n\n')
	data = list(filter(lambda l: len(l) > 6, list(map(lambda x: x.split(), data))))
	valid_count = 0
	for pp in data:
		if len(pp) == 8:
			valid_count += 1
		else:
			if 'cid' not in list(map(lambda field: field[0:3], pp)):
				valid_count += 1
	print(valid_count)

with open('input', 'r') as f:
	data = f.read().split('\n\n')
	data = list(filter(lambda l: len(l) > 6, list(map(lambda x: x.split(), data))))
	valid_count = 0
	for pp in data:
		if len(pp) == 8 or 'cid' not in list(map(lambda field: field[0:3], pp)):
			valid: bool = True
			for field in pp:
				prefix = field[0:3]
				content = field[4:]
				if prefix == 'byr':
					if len(content) != 4 or not (1920 <= int(content) <= 2002):
						valid = False
						break
				if prefix == 'iyr':
					if len(content) != 4 or not (2010 <= int(content) <= 2020):
						valid = False
						break
				if prefix == 'eyr':
					if len(content) != 4 or not (2020 <= int(content) <= 2030):
						valid = False
						break
				if prefix == 'hgt':
					units = content[-2:]
					if units == 'cm' and not (150 <= int(content[:-2]) <= 193):
						valid = False
						break
					elif units == 'in' and not (59 <= int(content[:-2]) <= 76):
						valid = False
						break
					elif units != 'cm' and units != 'in':
						valid = False
						break
				if prefix == 'hcl':
					if content[0] != '#' or len(content) != 7 or not all(c in string.hexdigits for c in content[1:]):
						valid = False
						break
				if prefix == 'ecl':
					if content not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
						valid = False
						break
					print(content)
				if prefix == 'pid':
					if len(content) != 9 or not str.isdigit(content):
						valid = False
						break
			if valid:
				valid_count += 1
				print(pp)
	print(valid_count)