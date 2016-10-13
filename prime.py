#!/usr/bin/env python
# Find all primes in a range using the Sieve of Eratosthenes.
# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def SieveOfEratosthenes(start, stop):
    numList = __build__(start, stop)
    return __sieve__(numList)
    
def __build__(start, stop):
    numList = []
    for x in range(start, stop):
        numList.append(x)
    return numList
    
def __sieve__(numList):
    if 1 in numList:
        numList.remove(1)
    for multiplier in range(2, 11):
        if not multiplier%2 == 0 or multiplier == 2: # only test prime dividers
            for num in numList:
                if num%multiplier == 0 and not num == multiplier:
                    numList.remove(num)
    return numList

if __name__ == '__main__':
    start = input("Start number: ")
    stop = input("End number: ")
    print SieveOfEratosthenes(start, stop)
