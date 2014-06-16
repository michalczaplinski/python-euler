import math

trues = { i:True for i in range(2, 2000001) }
nums = range(2, 2000001)

for i in nums:
    if trues[i] == True:
        for j in range(i*i, 2000001, i):
            trues[j] = False

print sum(( k for k, v in trues.iteritems() if v == True ))
