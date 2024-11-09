#number = int(input('Give me a number and ill tell you if its Odd or Even! '))
#if number % 2 == 0:
#    print(f'The number {number} is Even')
#else:
#    print(f'The number {number} is Odd')
from distutils.command.check import check


def question():
    number = int(input('Give me a number and ill tell you if its Odd or Even! '))
    def numbers():
        if number % 2 == 0:
            print(f'The number {number} is Even')
        else:
            print(f'The number {number} is Odd')
    numbers()

question()