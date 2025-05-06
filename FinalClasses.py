#This is the class program for my final project
#Bonuses I plan on using are randomness and puzzles
#You will come across an old house in a neighborhood, and it is your choice whether or not you go in
#But if you do, its like a casino but not as much where you can gamble, but you can go to different parts and rooms
#games like roulette, higher or lower, etc.
#it needs atleast 12 rooms/interactions

#classes are gonna be player, main game loop, the rooms, and the games.

class Player:
    #player will manage the player, and the amount of money the player has
    def __init__(self):
        self.name = ''
        self.balance = 100     #starting balance
        
    def update_balance(self, amount):
        self.balance += amount
        print(f'Your new balance is ${self.balance}.')

class RunGame:
    pass

class HigherOrLower:
    pass

class Roulette:
    pass

class E:
    pass
