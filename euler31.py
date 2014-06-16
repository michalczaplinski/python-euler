
perms = 0
total = 0

def countPennies():
    for i in range(0, 201, 100):
        total += i
        for j in range(0, 201, 50):
            total += j
            for k in range(0, 201, 20):
                total += k
                for l in range(0, 201, 10):
                    total += l
                    for m in range(0, 201, 5):
                        total += m
                        for n range(0, 201, 2):
                            total += n
                            for o in range(0, 201):
                                total += o
                                if total == 200:
                                    perms += 1
                                elif total > 200:



