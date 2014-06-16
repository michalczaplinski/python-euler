maximum = 0

for i in range(13, 1000000):

    n = i
    steps = 0
    while True:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n+1
        steps+=1
        if n == 1:
            break

    if steps > maximum:
        maximum = steps
        best = i

print best