with open('input', 'r') as f:
	data = list(map(lambda x: set(x.replace('\n', '')), f.read().split('\n\n')))
	count = 0
	for s in data:
		count += len(s)
	print(count)

with open('input', 'r') as f:
	data = list(map(lambda x: x.strip().split('\n'), f.read().split('\n\n')))
	count = 0
	for s in data:
		if len(s) == 1:
			count += len(s[0])
		else:
			intr = set(s[0]).intersection(*s[1:])
			count += len(intr)
	print(count)