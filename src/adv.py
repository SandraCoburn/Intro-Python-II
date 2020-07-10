from room import Room
from player import Player
from pprint import pprint as pp
#from snake import main
import snake
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"), 

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
room['foyer'].items = [Item("bracelete", "gold"), Item("backpack", "leather backpack")]
room['overlook'].items = [Item("parrot", "small parrot"), Item("snake", "pretty snake")]
room['narrow'].items = [Item("rock", "lucky rock"), Item("stick", "wood stick")]
room['treasure'].items = [Item("ring", "emerald ring"), Item("necklace", "pearls necklace")]

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

#to change the text color in terminal
def esc(code):
    return f'\033{code}m'


def game():
    room_name = "outside"
    directions = ["n", "s", "e", "w"]
    yes_no = ["yes", "no"]
    current_room = room[room_name]

    #introduction: 
    name = input("What is your name?\n")
    if len(name) > 0:  
        player1 = Player(name, current_room)
        pp(f"Greetings, {player1.name.upper()}! Let us start the adventure!")
       
        #Start of game:
        response = ""
        while response not in yes_no:
            response = input("Would you like to start the game?\nyes/no\n")
            if response == "yes":
                print("*********************************************************")
                pp("You will step into the first room. What are you gonna find?")
            elif response == "no":
                pp("You are not ready for this adventure. Good bye!")
                quit()
            else: 
                print("I didn't understant that. Type yes or no. \n")
        while True:
            #print(f"You are currently in {player1.current_room}")
            print(player1)
            print("***************************************************************")
            response = input("Which direction you want to go?\n pick one: [n], [s], [e] or [w] or [q] to exit\n").strip().lower().split()[0]
            response = response[0]
            pp(f"ok so you want to go {response}")
            print("****************************************")
            if response == "q":
                print(f"Good bye {player1.name}")
                exit(0)
            elif response in directions:
                player1.move(response)
                if player1.current_room == room["foyer"]:
                    for i, p in enumerate(room['foyer'].items):
                        print(f"{i + 1} - {p}")
                    selection = input("Which item do you want? [1/2]\n")
                    player1.add_to_items(room["foyer"].items[int(selection)-1])
                    print()
                    print(f"you picked the {player1.items[0].name}!")
                    print("*********************************************e")
                    print()
                    #pass #snake.main(1)
                elif player1.current_room == room["overlook"]:
                    for i, p in enumerate(room['overlook'].items):
                        print(f"{i + 1} - {p}")
                    selection = input("Which item do you want? [1/2]\n")
                    player1.add_to_items(room["foyer"].items[int(selection)-1])
                    print()
                    print(f"you picked the {player1.items[0].name}!")
                    print("*********************************************e")
                    print()
                elif player1.current_room == room["narrow"]:
                    for i, p in enumerate(room['narrow'].items):
                        print(f"{i + 1} - {p}")
                    selection = input("Which item do you want? [1/2]\n")
                    player1.add_to_items(room["foyer"].items[int(selection)-1])
                    print()
                    print(f"you picked the {player1.items[0].name}!")
                    print("*********************************************e")
                    print()
                elif player1.current_room == room["treasure"]:
                    for i, p in enumerate(room['treasure'].items):
                        print(f"{i + 1} - {p}")
                    selection = input("Which item do you want? [1/2]\n")
                    player1.add_to_items(room["foyer"].items[int(selection)-1])
                    print()
                    print(f"you picked the {player1.items[0].name}!")
                    print("*********************************************e")
                    print(f"you have all these items: {len(player1.items)}")
                    for n, i in enumerate(player1.items):
                        print(f"{n + 1} - {i}")
                    drop_item = input("To go back, you need to drop one item. Which one you pick?\n")
                    player1.drop_from_items(player1.items[int(drop_item)-1])
                    print("***************************************************")
            else:
                pp("I didn't understand that. Enter [n, s, e, or w] to move or [q] to quit.\n")
        pp("Thanks for playing!")
    else:
        pp("You need to provide your name. Try again!")
game()


