#!/usr/bin/python3
"""
this is the prime number interview
question understood
"""


def is_prime(number):
    """
    is prime method
    """
    if number <= 1:
        return False
    # Check for divisors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    # If no divisors were found, the number is prime
    return True


def isWinner(x, nums):
    """
    method to find the
    winner in all the rounds
    """
    player_dic = {"maria": 0, "ben": 0}
    gamer = 1
    ben = 0
    maria = 0
    for i in nums:
        arr = []
        for j in range(2, i + 1):
            arr.append(j)

        for item in arr:
            if is_prime(item):
                num = item
                if gamer % 2 == 0:
                    ben = ben + 1
                else:
                    maria = maria + 1

                for a in arr:
                    if num % a == 0:
                        arr.remove(a)
                gamer = gamer + 1
            break

        if (maria > ben):
            player_dic['maria'] = player_dic['maria'] + 1
        else:
            player_dic['ben'] = player_dic['ben'] + 1
        maria = 0
        ben = 0
    if (player_dic['maria'] > player_dic['ben']):
        return "Maria"
    elif (player_dic['maria'] < player_dic['ben']):
        return "Ben"
    else:
        return None
