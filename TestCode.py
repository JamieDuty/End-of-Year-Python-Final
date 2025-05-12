import random
#need to add a way to count up wins so I can add secret keys and things
class Game:
    def __init__(self, player):
        self.player = player
        self.house = House()

    def start(self):
        print("You have suddenly found yourself in an old strange neighborhood.")
        print("It all looks so uniform and strange, except one house just feels... different. You decide to go up to it to take a closer look.")
        choice = input("Do you want to enter the house? (yes/no): ").lower()
        if choice == 'yes':
            self.house.enter(self.player)
        else:
            print("You walk away and miss the opportunity... maybe next time.")

class Room:
    def __init__(self, name):
        self.name = name
        self.exits = {}
        
    def connect(self, direction, room):
        self.exits[direction] = room
    
    def get_exit(self, direction):
        return self.exits.get(direction)
    
    def play(self, player):
        pass

class Player:
    def __init__(self, name):
        self.name = name
        self.coins = 100  #the player starts with 100 dabloons
        self.inventory = []

    def add_coins(self, amount):
        self.coins += amount

    def spend_coins(self, amount):
        if self.coins >= amount:
            self.coins -= amount
            return True
        else:
            print("You are out of dabloons!")
            return False

class SlotMachine(Room):
    def __init__(self):
        super().__init__('Slot Machine Room')
    
    def play(self, player):
        #Welcome message used to get here
        #Add detail here
        print("With shaky hands, you pull the lever, and the slots begins spinning....")
        print("every passing spin, the nerves rise.")
        print("At last, the results.....")
        
        if not player.spend_coins(10):
            return
        symbols = ['Cherry', 'Lemon', 'Bell']
        result = [random.choice(symbols) for i in range(3)]
        print(' | '.join(result))
        if len(set(result)) == 1:
            print("\nJackpot! You win 50 Dabloons!")
            player.add_coins(50)
        else:
            print("\nBetter luck next time.")
        print(f"You now have {player.coins} dabloons.")

class DiceGame(Room):
    def __init__(self):
        super().__init__('Dice Game Room')

    def play(self, player):
        #Add detail here
        if not player.spend_coins(5):
            return
        player_roll = random.randint(1, 6)
        house_roll = random.randint(1, 6)
        print(f'\nYou rolled: {player_roll}')
        print(f'House rolled: {house_roll}')
        if player_roll > house_roll:
            print('\nYou win 10 dabloons!')
            player.add_coins(10)
        else:
            print("\nYou lose!")
        print(f"You now have {player.coins} dabloons.")
            
class House:
    def __init__(self):
        # Create rooms
        self.slot_room = SlotMachine()
        self.dice_room = DiceGame()
        self.entrance = Room("Entrance")

        # Connect rooms
        self.entrance.connect("north", self.slot_room)
        self.entrance.connect("east", self.dice_room)
        self.slot_room.connect("south", self.entrance)
        self.dice_room.connect("west", self.entrance)

        self.current_room = self.entrance

    def enter(self, player):
        print("You enter the house. It's dark and mysterious.")
        self.move(player)

    def move(self, player):
        while True:
            print(f"\nYou are in the {self.current_room.name}.")
            if isinstance(self.current_room, Room) and hasattr(self.current_room, 'play') and self.current_room.name != "Entrance":
                while True:
                    self.current_room.play(player)
                    again = input("Play again? (yes/no): ").lower()
                    while again.lower() != 'yes' and again.lower() != 'no':
                        again = input("Play again? (yes/no): ").lower()    
                    if again != "yes":
                        break
            print("Available directions:")
            for direction in self.current_room.exits:
                print(f"- {direction.title()}")
            print("- Leave (to exit the house)")

            choice = input("What direction do you want to go? ").lower()
            if choice == "leave":
                print("You leave the house and step back into reality. The night is over.")
                break
            elif choice in self.current_room.exits:
                self.current_room = self.current_room.get_exit(choice)
            else:
                print("You can't go that way.")
