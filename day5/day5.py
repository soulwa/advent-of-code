import math

def calc_seat_id(instr):
	lrow = 0
	hrow = 127
	lcol = 0
	hcol = 7
	col = 0
	row = 0
	for c in instr[0:6]:
		if c == 'F':
			hrow = math.floor((lrow + hrow) / 2)
		elif c == 'B':
			lrow = math.ceil((lrow + hrow) / 2)
	if instr[6] == 'F':
		row = lrow
	else:
		row = hrow
	for c in instr[7:9]:
		if c == 'L':
			hcol = math.floor((lcol + hcol) / 2)
		elif c == 'R':
			lcol = math.ceil((lcol + hcol) / 2)
	if instr[9] == 'L':
		col = lcol
	else:
		col = hcol
	return row * 8 + col


with open('input', 'r') as f:
	instrs = [line for line in f]
	print(max(list(map(calc_seat_id, instrs))))

with open('input', 'r') as f:
	seats_lookup = dict()
	for line in f:
		seat_id = calc_seat_id(line)
		seats_lookup[seat_id] = seat_id
	for k in seats_lookup:
		if k + 1 not in seats_lookup and k + 2 in seats_lookup:
			print(k + 1)
