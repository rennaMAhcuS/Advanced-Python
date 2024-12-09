"""
NCERT Question.

Write a program that creates a GK quiz consisting of any five questions of your choice.
The questions should be displayed randomly. Create a user defined function score() to
calculate the score of the quiz and another user defined function remark(score_value)
that accepts the final score to display remarks as follows:
5 - Outstanding
4 - Excellent
3 - Good
2 - Read more to score more
1 - Need to take interest
0 - General knowledge will always help you. Take it seriously.
"""
from random import randint

Questions = ["Capital of Japan: ",
             "Smallest country: ",
             "Most populous country: ",
             "National bird: ",
             "Where were Olympic games conducted in 2012? "]


# Helps in Calculating Score
def score(question_number, answer):
    if question_number == 1 and answer == "tokyo":
        return True
    elif question_number == 2 and answer == "vatican city":
        return True
    elif question_number == 3 and answer == "china":
        return True
    elif question_number == 4 and answer == "peacock":
        return True
    elif question_number == 5 and answer == "london":
        return True
    else:
        return False


# Final Remark
def remark(score_value):
    if score_value == 5:
        print("Outstanding!")
    elif score_value == 4:
        print("Excellent!")
    elif score_value == 3:
        print("Good.")
    elif score_value == 2:
        print("Read more to score more.")
    elif score_value == 1:
        print("Need to take interest.")
    elif score_value == 0:
        print("General knowledge will always help you. Take it seriously.")


NotAsked = [1, 2, 3, 4, 5]
Score = 0

for i in range(5, 0, -1):
    position = randint(1, i)
    Answer = input((Questions[NotAsked[position - 1] - 1]))
    if score(NotAsked[position - 1], Answer.lower()):
        Score += 1
    NotAsked.pop(position - 1)

print("Your Score is", Score)
remark(Score)
