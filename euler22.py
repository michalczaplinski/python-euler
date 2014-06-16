import string

with open("names.txt", 'r') as f:
    text = sorted([ x.strip ('"') for x in f.read().split(',') ])

total = 0   
for name in text:
    score = (text.index(name)+1) * sum([ (string.ascii_uppercase.index(x)+1) for x in name])
    total += score

print total