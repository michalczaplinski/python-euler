#!/usr/bin/python
import copy

r1 = '75'
r2 = '95 64'
r3 = '17 47 82'
r4 = '18 35 87 10'
r5 = '20 04 82 47 65'
r6 = '19 01 23 75 03 34'
r7 = '88 02 77 73 07 63 67'
r8 = '99 65 04 28 06 16 70 92'
r9 = '41 41 26 56 83 40 80 70 33'
r10 = '41 48 72 33 47 32 37 16 94 29'
r11 = '53 71 44 65 25 43 91 52 97 51 14'
r12 = '70 11 33 28 77 73 17 78 39 68 17 57'
r13 = '91 71 52 38 17 14 91 43 58 50 27 29 48'
r14 = '63 66 04 68 89 53 67 30 73 16 69 87 40 31'
r15 = '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

lines = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15]
lines = [ r.split(' ') for r in lines ]

path = 0
for i in range(15):
    for j in range(i):
        path += lines[i]

for index, l in enumerate(lines):
    print (len(lines)-index)*2*' ' + '  '.join(l)

