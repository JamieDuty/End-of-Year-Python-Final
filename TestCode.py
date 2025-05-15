import random
#lot of youtube and google was needed to fully understand this
#so basically i say i understand it but not 100%
#this game is basically rng based

#Base Room class has directions to other rooms
class Room:
    def __init__(self, name):
        self.name = name
        self.exits = {} #This dictionary stores the directions and connected rooms together

    def connect(self, direction, room):
        self.exits[direction] = room

    def get_exit(self, direction):
        return self.exits.get(direction)

    def play(self, player):
        pass #Base room doesn't do anything with the game so we just pass it

#Player class to hold player info, currency, and keys
class Player:
    def __init__(self, name):
        self.name = name
        self.coins = 100 #You start with 100 dabloons!
        self.inventory = []
        #Track the wins in each type of game
        self.wins = {
            "slot": 0,
            "dice": 0,
            "card": 0,
            "guess": 0,
            "quiz": 0,
            "flip": 0,
            "riddle": 0
        }
        self.keys = set() #Set of secret room keys for win you win each game
    
    #These control when you add or spend coins
    def add_coins(self, amount):
        self.coins += amount

    def spend_coins(self, amount):
        if self.coins >= amount:
            self.coins -= amount
            return True
        else:
            print("You are out of dabloons!")
            return False
    
    #When you win each type of game it adds
    #and when you win 3 of that type you get the secret room key!
    def add_win(self, game_type):
        self.wins[game_type] += 1
        print(f"You have {self.wins[game_type]} win(s) in {game_type}.")
        if self.wins[game_type] == 3:
            key = f"{game_type}_key"
            self.keys.add(key)
            print(f"You've earned a key to the {game_type} secret room!")

#These games are subclasses of the room class
#Each game is very similar to eachother, being ran off a random
#Number generation basically.
#this is the slot machine room
#you must get all 3 the same to win
class SlotMachine(Room):
    def __init__(self):
        super().__init__('Slot Machine Room')

    def play(self, player):
        print("With shaky hands, you pull the lever, and the slots begins spinning....")
        print("Every passing spin, the nerves rise. At last, the results.....")
        if not player.spend_coins(10):
            return
        symbols = ['Cherry', 'Lemon', 'Bell']
        result = [random.choice(symbols) for _ in range(3)]
        print(" | ".join(result))
        if len(set(result)) == 1:
            print("Jackpot! You win 50 dabloons!")
            player.add_coins(50)
            player.add_win("slot")
        else:
            print("Better luck next time.")
        print(f"You now have {player.coins} dabloons.")

#The dice game room
#You have to roll higher than the dealer to win
class DiceGame(Room):
    def __init__(self):
        super().__init__('Dice Game Room')

    def play(self, player):
        if not player.spend_coins(5): return
        roll_player = random.randint(1, 6)
        roll_house = random.randint(1, 6)
        print(f"You rolled: {roll_player}, House rolled: {roll_house}")
        if roll_player > roll_house:
            print("You win 10 dabloons!")
            player.add_coins(10)
            player.add_win("dice")
        else:
            print("You lose.")
        print(f"You now have {player.coins} dabloons.")

#This is the card game room
#you must get a higher card than the dealer
class CardGame(Room):
    def __init__(self):
        super().__init__('Card Game Room')

    def play(self, player):
        if not player.spend_coins(10): return
        card_player = random.randint(1, 13)
        card_house = random.randint(1, 13)
        print(f"You drew a {card_player}, House drew a {card_house}")
        if card_player > card_house:
            print("You win 20 dabloons!")
            player.add_coins(20)
            player.add_win("card")
        else:
            print("House wins.")
        print(f"You now have {player.coins} dabloons.")

#this is the guess number game
#you must guess the number to win
class GuessNumber(Room):
    def __init__(self):
        super().__init__('Guess the Number Room')

    def play(self, player):
        if not player.spend_coins(5): return
        number = random.randint(1, 5)
        guess = int(input("Guess a number between 1 and 5: "))
        if guess == number:
            print("Correct! You win 15 dabloons!")
            player.add_coins(15)
            player.add_win("guess")
        else:
            print(f"Wrong! The number was {number}.")
        print(f"You now have {player.coins} dabloons.")

#this is the quiz game room
#you must answer the very simple question to win
#i ran out of time to add to this and add more questions :(
class QuizGame(Room):
    def __init__(self):
        super().__init__('Quiz Room')

    def play(self, player):
        if not player.spend_coins(5): return
        q = ("What is 2+2?", "4")
        answer = input(q[0] + " ")
        if answer.strip() == q[1]:
            print("Correct! You win 10 dabloons!")
            player.add_coins(10)
            player.add_win("quiz")
        else:
            print("Incorrect.")
        print(f"You now have {player.coins} dabloons.")

#this is the coin flip room
#you must call what the coin lands to win
class CoinFlip(Room):
    def __init__(self):
        super().__init__('Coin Flip Room')

    def play(self, player):
        if not player.spend_coins(5): return
        choice = input("Heads or Tails? ").lower()
        result = random.choice(["heads", "tails"])
        print(f"Coin shows: {result}")
        if choice == result:
            print("You win 10 dabloons!")
            player.add_coins(10)
            player.add_win("flip")
        else:
            print("You lose.")
        print(f"You now have {player.coins} dabloons.")

#this is the riddle room
#you must answer this riddle to win
#again i ran out of time to work on this :(
#wouldve added more riddles
class RiddleRoom(Room):
    def __init__(self):
        super().__init__('Riddle Room')

    def play(self, player):
        if not player.spend_coins(5): return
        riddle = ("What has to be broken before you can use it?", "egg")
        answer = input(riddle[0] + " ").strip().lower()
        if answer == riddle[1]:
            print("Correct! You win 15 dabloons!")
            player.add_coins(15)
            player.add_win("riddle")
        else:
            print("Incorrect. The answer was 'egg'.")
        print(f"You now have {player.coins} dabloons.")

#Secret Room accessible only if player has a key by winning that game 3 times
class SecretRoom(Room):
    def __init__(self, game_type):
        super().__init__(f'Secret {game_type.title()} Room')
        self.required_key = f"{game_type}_key"
        
    #if you enter the room with the key or you can't because you don't have the key
    def play(self, player):
        if self.required_key in player.keys:
            print(f"Welcome to the secret {self.name}. You found a treasure chest! +100 coins!")
            player.add_coins(100)
        else:
            print("You don’t have the key to this secret room.")

#House manages all rooms and navigation
#it holds all rooms and where they are relative to eachother
class House:
    def __init__(self):
        self.rooms = {
            "entrance": Room("Entrance"),
            "north": SlotMachine(),
            "east": DiceGame(),
            "west": CardGame(),
            "south": GuessNumber(),
            "northeast": QuizGame(),
            "northwest": CoinFlip(),
            "southeast": RiddleRoom(),
            #pretty sure my code doesn't recognize these rooms 
            #as connected to the rest of the house
            "secret_slot": SecretRoom("slot"),
            "secret_dice": SecretRoom("dice"),
            "secret_card": SecretRoom("card"),
            "secret_quiz": SecretRoom("quiz"),
            "secret_flip": SecretRoom("flip"),
            "secret_riddle": SecretRoom("riddle")
        }

        self.rooms["entrance"].connect("north", self.rooms["north"])
        self.rooms["entrance"].connect("east", self.rooms["east"])
        self.rooms["entrance"].connect("west", self.rooms["west"])
        self.rooms["entrance"].connect("south", self.rooms["south"])
        self.rooms["east"].connect("south", self.rooms["southeast"])
        self.rooms["north"].connect("east", self.rooms["northeast"])
        self.rooms["north"].connect("west", self.rooms["northwest"])

        self.rooms["north"].connect("secret", self.rooms["secret_slot"])
        self.rooms["east"].connect("secret", self.rooms["secret_dice"])
        self.rooms["west"].connect("secret", self.rooms["secret_card"])
        self.rooms["northeast"].connect("secret", self.rooms["secret_quiz"])
        self.rooms["northwest"].connect("secret", self.rooms["secret_flip"])
        self.rooms["southeast"].connect("secret", self.rooms["secret_riddle"])

        self.current_room = self.rooms["entrance"]
    
    #When you first enter the house
    def enter(self, player):
        print("You enter the house. It's dark and mysterious.")
        print("\nBut you hear lots of sounds coming from all around you.... ")
        print("You begin to explore")
        self.move(player)
    
    #manage where you move AND if you want to play again
    def move(self, player):
        while True:
            #basically just a fancy way to see if you played and aren't in the entrance, it will ask if you want to play again
            print(f"\nYou are in the {self.current_room.name}.")
            if isinstance(self.current_room, Room) and hasattr(self.current_room, 'play') and self.current_room.name != "Entrance":
                while True:
                    self.current_room.play(player)
                    again = input("Play again? (yes/no): ").lower()
                    if again != "yes":
                        break
            #prints the available directions or you can just leave and quit
            print("Available directions:")
            for direction in self.current_room.exits:
                print(f"- {direction.title()}")
            print("- Leave (to exit the house)")
            
            #handles where you want to go or if you want to leave
            choice = input("What direction do you want to go? ").lower()
            if choice == "leave":
                print("You leave the house and step back into reality. The night is over.")
                break
            elif choice in self.current_room.exits:
                self.current_room = self.current_room.get_exit(choice)
            else:
                print("You can't go that way.")

#Main Game class
#you start the game off with this class
class Game:
    def __init__(self, player):
        self.player = player
        self.house = House()

    def start(self):
        print("You have suddenly found yourself in an old strange neighborhood.")
        print("You look down and you find 100 dabloons..... strange.")
        print("You go ahead and pick them up with a strange feeling you may need them later..")
        print()
        print()
        print("You take a look around.")
        print("It all looks so uniform and strange, except one house just feels... different. You decide to go up to it to take a closer look.")
        choice = input("Do you want to enter the house? (yes/no): ").lower()
        if choice == 'yes':
            self.house.enter(self.player)
        else:
            print("You walk away and miss the opportunity... maybe next time.")

