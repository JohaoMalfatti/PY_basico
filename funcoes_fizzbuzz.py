from random import randint
class fizzbuss:
    def fb(n):
        if n % 3 == 0 and n % 5 == 0:
            return (f'FizzBuzz, {n} É divisivel por 3 e 5')
        if n % 5 == 0:
            return (f'Buzz, {n} É divisivel por 5')
        if n % 3 == 0:
            return(f'Fizz, {n} É divisel por 3')
    for i in  range (100):
        randon = randint(0,100)
        print (fb(randon))