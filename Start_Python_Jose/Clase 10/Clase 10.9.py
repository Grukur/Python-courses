
# ejecricio FitzBuzz
"""for i in range(1,101):
    if i % 3 == 0 and i % 5 ==0:
        print('FizzBuzz')
    elif i % 5 ==0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)"""



"""import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

print('the winning numbers are:',lottery_numbers,'\n')

top_player = players[0]
for i in players:
    match = len(i['numbers'].intersection(lottery_numbers))
    if match > len(top_player['numbers'].intersection(lottery_numbers)):
        top_player = i

winnings = 100 ** len(top_player['numbers'].intersection(lottery_numbers))

print(f"{top_player['name']} won {winnings}.")
print(f"{top_player['name']} won {winnings} with this numbers {top_player['numbers']} and {match} correct numbers.")"""


##################################

"""
Take a look at the code in the problem description where we test if a number is prime.
Refactor the code and put it into the function below to turn the prime_generator() function into a generator.

Implement your generator so that others can get a prime number generator like this:

g = prime_generator(100)    # g can generate prime numbers under 100
next(g) # get next prime like this

Reminder: you don't need to change the function name nor the argument
"""
"""def prime_generator(bound):
    for n in range(2, bound):
        for x in range(2, n):
            if n % x == 0:  # if n is divisible by x, it means it's not a prime number.
                break
        else:  # if n was not divisible by any x, it means it is a prime number.
            yield n

g = prime_generator(100)
next(g)"""

################################## Define un generador
"""
class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):  # always search from current start (inclusive) to stop (exclusive)
            for x in range(2, n):
                if n % x == 0:  # not prime
                    break
            else:  # n is prime, because we've gone through the entire loop without having a non-prime situation
                self.start = n + 1  # next time we need to start from n + 1, otherwise we will be trapped on n
                return n  # return n for this round
        raise StopIteration()  # this is what tells Python we've reached the end of the generator
    """

