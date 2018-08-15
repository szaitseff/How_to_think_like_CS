#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      admin
#
# Created:     19.01.2018
# Copyright:   (c) admin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1.
    It was first posed by a German mathematician called Lothar Collatz:
    the Collatz conjecture (aka 3n+1 conjecture), is that this sequence
    terminates for all positive values of n. So far, no one has been able
    to prove it or disprove it!
    """
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:              # n is even
            n = n // 2
        else:                       # n is odd
            n = n * 3 + 1
    print(n, end=".\n")

seq3np1(3)
