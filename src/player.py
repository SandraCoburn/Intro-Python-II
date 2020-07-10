# Write a class to hold player information, e.g. what room they are in
# currently.
from snake import main
class Player:
    def __init__(self, name, current_room, items=[]):
        self.items = items
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        attribute = direction + '_to'

        if hasattr(self.current_room, attribute):
            self.current_room = getattr(self.current_room, attribute)


        # if getattr(self.current_room, f'{direction}_to'):
        #     current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print("Sorry, you cannot move in that direction")

    def add_to_items(self, item):
        #if player choose a number he can chose  a guessing name to win the item
        self.items.append(item)

    def drop_from_items(self, item):
        self.items.remove(item)
    
    def __str__(self):
        return f"{self.name.upper()} is in {self.current_room}. {self.name.upper()} has {len(self.items)} items"
       
    