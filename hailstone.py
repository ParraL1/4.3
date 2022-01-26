#Name: Lilliana Parra
#Github Username: ParraL1
#Date: 01/26/2022
#Description: Write a function named hailstone that takes a positive integer parameter as the initial number of a hailstone sequence and returns how many steps it takes to reach 1


def hailstone(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count