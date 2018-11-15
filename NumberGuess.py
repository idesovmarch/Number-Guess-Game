(Code Academy Project)

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Enter your guess: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum roll value is %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "Invalid value"
  else:
    print "Rolling"
    sleep(2)
    print "You rolled a %d" % (second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print "The correct number was %d" % (total_roll)
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "You Won!"
    else:
      print "You Lost!"
  
roll_dice(20)
