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

#Name of the game is Secret Casino i guess
#Run the program to start it
#this game is mostly luck based
#lowkey haven't tested it so hoping everything works
#the goal is to unlock the secret rooms 
#overall this program worked well but for some reason you could get stuck in the secret rooms
#probably could've added more user control but it worked well and got a fair grade.
