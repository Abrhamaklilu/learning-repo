# print dir time))
def prime_finder_to(bound):
    primes = []
    find = 0
    number = 2
    while find < bound:
        for no in primes:
            if number % no == 0:
                break
        else:
            primes.append(number)
    number += 1
    return primes


prime_finder_to(1000)