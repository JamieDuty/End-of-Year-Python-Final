from TestCode import Player
from TestCode import Game

def main():
    #basically all main does is take your name and print the first message and it calls the game and player class
    #and the rest is run on the classes program
    
    #take input on player name
    name = input('What\'s your name? ')
    player = Player(name)
    #print the welcome message
    print()
    print(f'Welcome, {player.name}, the night is young, lets get started.')
    #start the game
    player = Player(name)
    game = Game(player)
    game.start()
if __name__ == '__main__':
    main()


#Run the program to start it
#this game is mostly luck based
#lowkey haven't tested it so hoping everything works
#the goal is to unlock the secret rooms 