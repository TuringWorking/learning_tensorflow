# Testing template for "Guess the number"

###################################################
# Student should add code for "Guess the number" here


# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


#import simplegui
import random
import math


secret_number = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print "New game. Range is from 0 to 100"
    global secret_number;
    secret_number = range100();


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    return random.randint(0,100)


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    return random.randint(0,1000)


#import Guess
def input_guess(guess):
    # main game logic goes here

    global secret_number;
    #secret_number = int( secret_number )
    guess = int(guess);
    print "Guess was", guess
    #new_game();
    print "Secret_number was", secret_number;

    if guess == secret_number:
        print "Correct!"
    elif guess < secret_number:
        print "Higher!"
    else:
        print "Lower!"



###################################################
# Start our test #1 - assume global variable secret_number
# is the the "secret number" - change name if necessary

new_game()
input_guess("50")
input_guess("75")
input_guess("62")
input_guess("68")
input_guess("71")
input_guess("18")
input_guess("74")

###################################################
# Output from test #1
#New game. Range is from 0 to 100
#Number of remaining guesses is 7
#
#Guess was 50
#Number of remaining guesses is 6
#Higher!
#
#Guess was 75
#Number of remaining guesses is 5
#Lower!
#
#Guess was 62
#Number of remaining guesses is 4
#Higher!
#
#Guess was 68
#Number of remaining guesses is 3
#Higher!
#
#Guess was 71
#Number of remaining guesses is 2
#Higher!
#
#Guess was 73
#Number of remaining guesses is 1
#Higher!
#
#Guess was 74
#Number of remaining guesses is 0
#Correct!
#
#New game. Range is from 0 to 100
#Number of remaining guesses is 7

###################################################
# Start our test #2 - assume global variable secret_number
# is the the "secret number" - change name if necessary

#range1000()
#secret_number = 375
#input_guess("500")
#input_guess("250")
#input_guess("375")

###################################################
# Output from test #2
#New game. Range is from 0 to 100
#Number of remaining guesses is 7
#
#New game. Range is from 0 to 1000
#Number of remaining guesses is 10
#
#Guess was 500
#Number of remaining guesses is 9
#Lower!
#
#Guess was 250
#Number of remaining guesses is 8
#Higher!
#
#Guess was 375
#Number of remaining guesses is 7
#Correct!
#
#New game. Range is from 0 to 1000
#Number of remaining guesses is 10



###################################################
# Start our test #3 - assume global variable secret_number
# is the the "secret number" - change name if necessary

#secret_number = 28
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")

###################################################
# Output from test #3
#New game. Range is from 0 to 100
#Number of remaining guesses is 7
#
#Guess was 50
#Number of remaining guesses is 6
#Lower!
#
#Guess was 50
#Number of remaining guesses is 5
#Lower!
#
#Guess was 50
#Number of remaining guesses is 4
#Lower!
#
#Guess was 50
#Number of remaining guesses is 3
#Lower!
#
#Guess was 50
#Number of remaining guesses is 2
#Lower!
#
#Guess was 50
#Number of remaining guesses is 1
#Lower!
#
#Guess was 50
#Number of remaining guesses is 0
#You ran out of guesses.  The number was 28
#
#New game. Range is from 0 to 100
#Number of remaining guesses is 7
