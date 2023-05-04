def parse_stack_text(stacktext):
    stacks = [""]*10
    for line in stacktext[:-1]:
        for i, box in enumerate(line[1::4]):
            if box != " ": stacks[i+1] += box
    return stacks
    
input_data = open("input.txt").read()
stackt, instructions = [part.split("\n") for part in input_data.split("\n\n")]
stacks = parse_stack_text(stackt)

p1, p2 = stacks[:], stacks[:]
for line in instructions:
    _, n, _, src, _, dest = line.split()
    n = int(n); src = int(src); dest = int(dest)

    p1[src], p1[dest] = p1[src][n:],  p1[src][:n][::-1] + p1[dest]
    p2[src], p2[dest] = p2[src][n:],  p2[src][:n]       + p2[dest]

print("Part 1:", "".join(s[0] for s in p1 if s))
print("Part 2:", "".join(s[0] for s in p2 if s))
