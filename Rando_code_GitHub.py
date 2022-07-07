#!/usr/bin/env python

# I want to play a game ...

from random import choice

print("Will you win the coin flip?")

coin_flip = choice(["Heads", "Tails"])

if coin_flip == "Heads":
    print("You win!")
else:
    print("You lose!")
