from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        # holds all discovered rooms
        self.rooms = {}
        # put player in starting room
        self.player = Player(world.starting_room)
        # prev room is set to starting room by default
        self.prev_room = self.player.current_room.id

                    # random direction
    def mapping(self, chosen_direction, first_room=False):
        self.prev_room = self.player.current_room.id

        if not first_room:
            # travel in chosen direction
            self.player.travel(chosen_direction)
            # add that direction to traveral path
            traversal_path.append(chosen_direction)
        # store the current room
        room_id = self.player.current_room.id

        # check if current room is in room, if not 
        if room_id not in self.rooms:
            # grab all possible compass directions, store in list
            directions = self.player.current_room.get_exits()
            # add current room to dictionary as key with empty dict as value
            self.rooms[room_id] = {}
            # loop through each possible direction
            for direction in directions:
                # create nested dict of direction inside room, with '?' as default direction value
                self.rooms[room_id][direction] = '?'

        if chosen_direction != None:
            if chosen_direction == 'n':
                self.rooms[room_id]['s'] == self.prev_room
            if chosen_direction == 's':
                self.rooms[room_id]['n'] == self.prev_room
            if chosen_direction == 'e':
                self.rooms[room_id]['w'] == self.prev_room
            if chosen_direction == 'w':
                self.rooms[room_id]['e'] == self.prev_room
            self.rooms[self.prev_room][chosen_direction] = room_id




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
