# TAKES A LONG TIME ~3-4 minutes

n = 2520
while True:
    if n % 1000000 == 0:
        print n
    for i in range(11, 21):
        if n % i == 0:
            continue
        else:
            n+=1
            break
    else:
        break

print n

#the result should be: 232 792 560