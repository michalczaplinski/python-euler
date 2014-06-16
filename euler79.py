
with open("keylog.txt", "r") as f:
    lines = [ line.rstrip('\n') for line in f ]


digits = []

for line in lines:
    for char in line:
        if char not in digits:
            digits.append(char)

order = {d: [] for d in digits}


candidates = []
for d in digits:
    for line in lines:
        if d in line:
            if line.index(d) == 0 and d not in candidates:
                candidates.append(d)

print candidates


for d in candidates[:]:
    for line in lines:
        if d in line and line.index(d) != 0:
            candidates.remove(d)
            break
