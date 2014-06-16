total = 1

for i in range(1, 101):
    total *= i

total = [ int(x) for x in str(total) ]

print sum(total)
