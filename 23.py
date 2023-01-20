# possible commands with their limitations (None for no limitation)
COMMANDS = ((lambda x: x+1, None), (lambda x: x*2, None))  # commands should be referring to a larger number
INTERVAL = (START, END) = 1, 30
TO_WALK_THROUGH = (15,)  # necessary to walk through  !!sorted!!
NOT_TO_WALK_THROUGH = tuple()  # impassible points

_intervals = []
_mapped_intervals = []
prev_point = START
for i in range(len(TO_WALK_THROUGH)):
    _intervals.append((prev_point, TO_WALK_THROUGH[i]))
    prev_point = TO_WALK_THROUGH[i]
_intervals += [(prev_point, END)]
for inter in _intervals:
    values = [[i, 1] if i == inter[1] else [i, 0] for i in range(inter[0], inter[1]+1)]
    for i in range(len(values)-2, -1, -1):
        val = values[i][0]
        if val in NOT_TO_WALK_THROUGH: continue
        for command in COMMANDS:
            new_val = command[0](val)
            if new_val <= inter[1]:
                values[i][1] += values[new_val-inter[0]][1]
    _mapped_intervals.append(values)
            # TODO: IMPLEMENT COUNTING THE USAGE OF A COMMAND
result = 1
for values in _mapped_intervals:
    result *= values[0][1]
print(result)
