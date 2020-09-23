"""
Author: Aidan Shannon
Program: validation_with_try.py
Date: 9/22/2020

program validates average scores and involves try and except if or if not to raise ValueError
"""
NUMBER_TESTS = 3


def average(score1, score2, score3):
    if score1 < 0 or score2 < 0 or score3 < 0:
        raise ValueError
    return float((score1 + score2 + score3)/NUMBER_TESTS)


if __name__ == '__main__':
    first_score = input("Enter first score: ")
    second_score = input("Enter second score: ")
    third_score = input("Enter third score: ")
    try:
        average_scores = average(int(first_score), int(second_score), int(third_score))
    except ValueError:
        print("Please enter positive scores only.")
    else:
        print("Average Grade: {}".format(average_scores))
