def run_program(prog):
	past_indicies = []
	i = 0
	acc = 0
	while i not in past_indicies and i < len(prog):
		instr = instrs[i]
		past_indicies.append(i)
		if instr[0] == 'acc':
			acc += int(instr[1])
			i += 1
		elif instr[0] == 'nop':
			i += 1
		elif instr[0] == 'jmp':
			i += int(instr[1])
	return (acc, i not in past_indicies)
		



with open('input', 'r') as f:
	instrs = [line.strip().split(' ') for line in f]
	print(run_program(instrs))
	for i in instrs:
		if i[0] == 'nop':
			i[0] = 'jmp'
			res = run_program(instrs)
			if res[1]:
				print(res[0])
				break
			else:
				i[0] = 'nop'
		elif i[0] == 'jmp':
			i[0] = 'nop'
			res = run_program(instrs)
			if res[1]:
				print(res[0])
				break
			else:
				i[0] = 'jmp'
