import itertools

with open("keylog.txt", "r") as f:
    LINES = [ line.rstrip('\n') for line in f ]

DIGITS = []
for line in LINES:
    for char in line:
        if char not in DIGITS:
            DIGITS.append(char)

perms = itertools.permutations(''.join(DIGITS), len(DIGITS))

for p in perms:
    for line in LINES:
        if p.index(line[0]) < p.index(line[1]) < p.index(line[2]):
            continue
        else: break
    else: break

print ''.join(p)













#CANDIDATES = []
#for d in DIGITS:
#    for line in LINES:
#        if d in line:
#            if line.index(d) == 0 and d not in CANDIDATES:
#                CANDIDATES.append(d)
#
#print CANDIDATES
#
#def findFirst(CANDIDATES, LINES, covered):
#    for d in CANDIDATES[:]:
#        for line in LINES:
#            line = line.strip(covered)
#            if d in line and line.index(d) != 0:
#                CANDIDATES.remove(d)
#    if
#        return findFirst(CANDIDATES, LINES, covered)
#
#    return covered
#
#print findFirst(CANDIDATES, LINES, '')
