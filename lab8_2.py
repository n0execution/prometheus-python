def is_even(num) :
    return (num % 2 == 0)




def find_fraction(summ):
    if type(summ) is not int or summ <= 2:
            return False
    

    num = summ / 2
    
    if is_even(summ) :
        numerator = num - 1

        if is_even(num - 1) :
            numerator = num - 2
    else :
        numerator = num

    denominator = summ - numerator

    return (numerator, denominator)



"""

10

1 + 9
2 + 8
3 + 7
4 + 6



13


1 + 12
2 + 11
3 + 10
4 + 9
5 + 8
6 + 7

"""