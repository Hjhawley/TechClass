# Author Info

__author__ = "d00453603@dixie.edu" # Hayden Hawley
__title__ = "Shrine of Anubis"
__description__ = "Find the treasure and escape the tomb in one piece."
__version__ = 1
__date__ = "Spring 2021"

import random

# Record Definitions

'''
Records:
    World:
        status (str): Whether or not the game is "playing", "win",
                      "quitting", or "lose". Initially "playing".
        world_map (dict[str: Location]): The lookup dictionary matching 
                                   location names to their
                                   information.
        player (Player): The player character's information.

    Player:
        alive (boolean): Whether the player is alive or dead.
        location (str): The name of the player's current location.
        inventory (list[str]): The player's collection of items.
                               Initially empty.

    Location:
        about (str): A sentence that describes what this location 
                     looks like.
        neighbors (list[str]): A list of the names of other places 
                               that you can reach from this 
                               location.
        loot (str): The tools or loot available at this location (if any.)
'''

# Core Game Functions

def exposition():
    
    # The message to be displayed at the start of the game.
    
    expo_text = "You find yourself lost in a dimly lit tomb.\n" \
                "Its builders are unknown to the modern world.\n" \
                "Your gut tells you there’s treasure nearby."
    return expo_text

def create_world():

    # Creates a new version of the world in its initial state.
    
    # Returns:
        # World: The initial state of the world
        
    world = {"status"    :
                "playing",
            "player"    : {
                "location"  : "rm_start",
                "inventory" : []},
            "world_map"       : [
                {"location"     : "rm_start",
                 "about"        : "You are in the central room. Light filters \n"
                                  "in through the ceiling. You see four doors, \n"
                                  "one in each direction. Which do you take?",
                 "neighbors"    : ["rm_gold", "rm_map", "rm_dark", "rm_torch"],
                 "loot"         : []},

                {"location"     : "rm_gold",
                 "about"        : "You find the gold! \n"
                                  "You hear a soft noise in the room to the west.",
                 "neighbors"    : ["", "rm_start", "", "death1"],
                 "loot"         : ["GOLD"]},

                {"location"     : "rm_map",
                 "about"        : "You find a dusty old map. This should help. \n"
                                  "(Enter \"MAP\" to check it.)",
                 "neighbors"    : ["rm_start", "", "death2", "rm_key"],
                 "loot"         : ["MAP"]},

                {"location"     : "rm_lit",
                 "about"        : "Your trusty torch lights the way. \n"
                                  "To the north you see a staircase. \n"
                                  "To the south you see a bottomless pit.",
                 "neighbors"    : ["rm_exit", "death2", "", "rm_start"],
                 "loot"         : []},
                
                {"location"     : "rm_dark",
                 "about"        : "You can’t see a thing. \n"
                                  "Do you risk fumbling around in the dark, or \n"
                                  "do you play it safe and turn back?",
                 "neighbors"    : ["rm_exit", "death2", "", "rm_start"],
                 "loot"         : []},

                {"location"     : "rm_torch",
                 "about"        : "You find a lit torch. \n"
                                  "You decide it's better not to question \n"
                                  "why it hasn't burnt out after all this time.",
                 "neighbors"    : ["death1", "rm_key", "rm_start", ""],
                 "loot"         : ["TORCH"]},
                
                {"location"     : "rm_key",
                 "about"        : "You find a key. But to what?",
                 "neighbors"    : ["rm_torch", "", "rm_map", ""],
                 "loot"         : ["KEY"]},
                
                {"location"     : "rm_exit",
                 "about"        : "You see an exit!",
                 "neighbors"    : ["", "rm_dark", "", ""],
                 "loot"         : []}
    ]}
    return world

def render(world):
    '''
    Consumes a world and produces a string that will describe the current state
    of the world. Does not print.
    
    Args:
        world (World): The current world to describe.
    
    Returns:
        str: A textual description of the world.
    '''
    loc = world["player"]["location"]
    for xdict in world["world_map"]:
        if xdict["location"] == loc:
            about = "============================================= \n" +xdict["about"]+"\n"
            for item in xdict["loot"]:
                if item not in world["player"]["inventory"]:
                    world["player"]["inventory"].append(item)
            about = about+"============================================="
            return about

    return "error"

def get_options(world):
    '''
    Consumes a world and produces a list of strings representing the options
    that are available to be chosen given this state.
    
    Args:
        world (World): The current world to get options for.
    
    Returns:
        list[str]: The list of commands that the user can choose from.
    '''
    loc = world["player"]["location"]
    options = []
    
    if loc == "rm_dark":
        options = ["TURN BACK", "RISK IT"]
    else:
        for xdict in world["world_map"]:
            if xdict["location"]  == loc:
                neighbors_pos = xdict["neighbors"]
        if neighbors_pos[0] != "":
            options.append("NORTH")
        if neighbors_pos[1] != "":
            options.append("SOUTH")
        if neighbors_pos[2] != "":
            options.append("EAST")
        if neighbors_pos[3] != "":
            options.append("WEST")
        if "MAP" in world["player"]["inventory"]:
            options.append("MAP")
    options.append("QUIT")
    return options

def update(world, command):
    '''
    Consumes a world and a command and updates the world according to the
    command, also producing a message about the update that occurred. This
    function should modify the world given, not produce a new one.
    
    Args:
        world (World): The current world to modify.
    
    Returns:
        str: A message describing the change that occurred in the world.
    '''
    loc = world["player"]["location"]
    if command == "QUIT":
        world["status"] = "quitting"
        return("Sorry to see you go!")
    elif world["player"]["location"] == "rm_start" and command == "NORTH":
        if "KEY" not in world["player"]["inventory"]:
            print("\nThe door seems to be locked. It won't budge.")
        else:
            print("\nYou try the key. It works!")
            for xdict in world["world_map"]:
                if xdict["location"]  == loc:
                    world["player"]["location"] = xdict["neighbors"][0]
    elif world["player"]["location"] == "rm_start" and command == "EAST":
        if "TORCH" not in world["player"]["inventory"]:
            for xdict in world["world_map"]:
                if xdict["location"]  == loc:
                    world["player"]["location"] = "rm_dark"
        else:
            for xdict in world["world_map"]:
                if xdict["location"]  == loc:
                    world["player"]["location"] = "rm_lit"
    elif command == "NORTH":
        for xdict in world["world_map"]:
            if xdict["location"]  == loc:
                world["player"]["location"] = xdict["neighbors"][0]
    elif command == "SOUTH":
        for xdict in world["world_map"]:
            if xdict["location"]  == loc:
                world["player"]["location"] = xdict["neighbors"][1]
    elif command == "EAST":
        for xdict in world["world_map"]:
            if xdict["location"]  == loc:
                world["player"]["location"] = xdict["neighbors"][2]
    elif command == "WEST":
        for xdict in world["world_map"]:
            if xdict["location"] == loc:
                world["player"]["location"] = xdict["neighbors"][3]
    elif command == "MAP":
        print(" _______\n"
              "| x G E |\n"
              "| T S D |\n"
              "| K M x |\n"
              "|_______|")
    elif command == "TURN BACK":
        world["player"]["location"] = "rm_start"
    elif command == "RISK IT":
        fumble = random.randrange(0, 3)
        if fumble == 0:
            for xdict in world["world_map"]:
                if xdict["location"]  == loc:
                    world["player"]["location"] = "death2"
                    print("\nWhat could go wrong?")
        elif fumble == 1:
            for xdict in world["world_map"]:
                if xdict["location"]  == loc:
                    world["player"]["location"] = "rm_start"
                    print("\nYou blindly fumble around and end up right where you started.")
        elif fumble == 2:
            for xdict in world["world_map"]:
                if xdict["location"]  == loc:
                    world["player"]["location"] = "rm_exit"
                    print("\nHere goes nothing!")
    if world["player"]["location"] == "death1":
        print("You are killed by venomous snakes. Bummer!")
        world["status"] = "lose"
    if world["player"]["location"] == "death2":
        print("You fall into a bottomless pit. Whoops.")
        world["status"] = "lose"
    if world["player"]["location"] == "rm_exit":
        world["status"] = "win"
    return ""

def render_ending(world):
    '''
    Create the message to be displayed at the end of your game.
    
    Args:
        world (World): The final world state to use in describing the ending.
    
    Returns:
        str: The ending text of your game to be displayed.
    '''
    if world["status"] == "win":
        if ("GOLD") in world["player"]["inventory"]:
            return "You see an exit! \nYou made it out with the gold! You're gonna be rich. \nThank you for playing."
        else:
            return "You see an exit! \nYou make it out alive! But without any treasure..."
    elif world["status"] == "lose":
        return "Try again!"
    else:
        return "Play again soon."

def choose(options, inventory):
    '''
    Consumes a list of commands, prints them for the user, takes in user input
    for the command that the user wants (prompting repeatedly until a valid
    command is chosen), and then returns the command that was chosen.
    
    Note:
        Use your answer to Programming Problem #42.3
    
    Args:
        options (list[str]): The potential commands to select from.
    
    Returns:
        str: The command that was selected by the user.
    '''
    print("COMMANDS:")
    for i in range(len(options)):
        print(" - "+options[i])
    if inventory != []:
        print("INVENTORY:")
        for i in range(len(inventory)):
            print(" - "+inventory[i])
    while True:
        command = input("What do you want to do? ")
        command = command.upper()
        if command in options:
            break
        print("  Invalid command.")

    return command

def main():

    # Run your game using the Text Adventure console engine.
    # Consumes and produces nothing, but prints and indirectly takes user input.

    print(exposition())
    world = create_world()
    while world["status"] == "playing":
        print(render(world))
        options = get_options(world)
        inventory = world["player"]["inventory"]
        command = choose(options, inventory)
        print(update(world, command))
    print(render_ending(world))
    input("Press any key to continue")

if __name__ == "__main__":
    main()