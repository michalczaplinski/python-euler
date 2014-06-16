from decimal import *
from time import sleep

getcontext().prec = 2000

largest_cycle_number = 7
largest_cycle_length = 6

for number in range(11, 1001):

    number_decimal = Decimal(1) / Decimal(number)
    number_string = str(number_decimal).split('.')[1][::-1]

    print number_string

    # arbitrary range
    for i in range(7, len(number_string)/2):
        if number_string[:i] == number_string[i:2*i]:

            if len(number_string[:i]) > largest_cycle_length:
                largest_cycle_length = i
                largest_cycle_number = number
            break

    print 'largest cycle', largest_cycle_number, largest_cycle_length
    #sleep(0.3)

