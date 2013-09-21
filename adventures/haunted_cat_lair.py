import random

# information about the game

rooms = {
    "start": {
        "description": "path by gate",
        "w": "gate",
        "n": "potion-poison trap",
    },
    "gate": {
        "description": "spikey iron gate",
        "e": "start",
    },
    "potion-poison trap": {
        "description": "cage with two bottles",
    },
    "portal": {
        "description": "a blue sparkly portal",
        "n": "joint",
        "e": "joint",
        "w": "joint",
        "s": "joint",
    },
    "joint": {
        "description": "a split in the path",
        "w": "winning room",
        "n": "poison shower trap",
    },
    "winning room": {
        "description": "Room with golden cat",
    },
    "poison shower trap": {
        "description": "Cage with vents",
    },
}

player = {
    "lives": 9,
}

objects = {
    "cage": {
        "vanished": False,
        "location": "potion-poison trap",
    },
    "potion": {
        "drunk": False,
        "location": "potion-poison trap",
    },
    "poison": {
        "drunk": False,
        "location": "potion-poison trap",
    },
    "crown": {
        "examine": "The crown is very sparkly",
        "location": "dalmatian prince",
    }
}

monsters = {
    "dalmatian prince": {
        "synonyms": ["dalmatian prince", "prince", "dalmatian", "dog"],
        "description": "You see a scary dalmatian prince wearing a crown. He doesn't drool.",
        "description dead": "You see a dalmatian prince lying on the floor. He isn't scary any more, and there's lots of drool.",
        "dying words": '"Lo! I am slain!" cries the dalmatian prince, as he falls to the floor.',
        "location": "winning room",
        "lives": 2,
        "strength": 2,
    },
}

# describing things

def describe(room):
    room_info = rooms[room]
    print(room_info["description"])
    for direction in ['e', 'w', 'n', 's']:
        exit = room_info.get(direction, None)
        if exit is not None:
            print("You can go ", direction)
    for monster_info in monsters.values():
        if monster_info["location"] == room:
            print(monster_info["description"])

# verbs

def move(room, direction):
    room_info =  rooms[room]
    new_room = room_info.get(direction, None)
    if new_room is None:
        print("I can't go that way.")
        return room
    else:
        if new_room == "potion-poison trap":
            print("a cage crashes down on you!")
        return new_room


def examine(room, object):
    if object in objects and objects[object]["location"] == room:
        description = objects[object].get("examine", "You see nothing special.")
        print(description)
    elif object in monsters and monsters[object]["location"] == room:
        description = monsters[object].get("examine", "You see nothing special.")
        print(description)
    else:
        print("I can't do that, silly human")


def lift(room, object):
    if object == "cage" and room == "potion-poison trap":
        if objects["cage"]["vanished"]:
            print("the cage is gone silly human")
        else:
            print("you can't lift it, you're too weak")
    else:
        print("I can't do that, silly human")


def drink(room, object):
    if object == "bottles" and room == "potion-poison trap":
        print("the cage vanishes but you lose a life")
        player["lives"] -= 1
        objects["cage"]["vanished"] = True
        objects["potion"]["drunk"] = True
        objects["poison"]["drunk"] = True
        rooms["potion-poison trap"]["n"] = "portal"
        rooms["potion-poison trap"]["s"] = "start"
        rooms["potion-poison trap"]["description"] = "A room with two bottles."
    else:
        print("I can't do that silly human")


def monster_dies(monster, room):
    monster_info = monsters[monster]
    # change the description
    monster_info["description"] = monster_info["dead description"]
    # drop anything the monster is carrying
    for object_info in objects.values():
        if object_info["location"] == monster:
            object_info["location"] = room
    # describe victory
    dying_words = monster_info.get("dying words", "You defeat the monster!")
    print(dying_words)


def fight(room, monster):
    monster_info = monsters.get(monster)
    if monster_info is not None and monster_info["location"] == room:
        outcomes = ["monster wins", "monster wins", "player wins", "player wins",
                    "tie", "special"]
        outcome = random.choice(outcomes)
        if outcome in {"player wins", "tie"}:
            monster_info["lives"] -= 1
            print("You hurt the monster")
        if outcome in {"monster wins", "tie"}:
            player["lives"] -= monster_info["strength"]
            print("The monster hurts you!")
            print("You have {} lives left.".format(player["lives"]))
        if outcome == "special":
            monster_info["lives"] = 0
            print("An amazing hit!  You win!")
        if monster_info["lives"] <= 0:
            monster_dies(monster, room)
    else:
        print("I can't do that, silly human")

# parsing of input

def determine_object(room, object):
    for object_name, object_info in objects.items():
        if object_info["location"] == room and object in object_info.get("synonyms", []):
            return object_name
    for object_name, object_info in monsters.items():
        if object_info["location"] == room and object in object_info.get("synonyms", []):
            return object_name
    return object


def parse(commands):
    commands = commands.lower()
    commands = commands.strip()
    words = commands.split()
    if len(words) == 1:
        command = words[0]
        object = None
    elif len(words) >= 2:
        command = words[0]
        object = " ".join(words[1:])
    else:
        command = None
        object = None
    return command, object

# main section

def start():
    print("Welcome! Your mission is to find the Golden Cat") 


def run():
    room = "start"
    while True:
        print()
        describe(room)
        commands = input("Enter command: ")
        command, object = parse(commands)
        object = determine_object(room, object)
        if command == "q" or command == "quit":
            break
        elif command in {"w", "e", "n", "s"}:
            room = move(room, command)
        elif command == "x" or command == "examine":
            examine(room, object)
        elif command == "l" or command == "lift":
            lift(room, object)
        elif command == "drink":
            drink(room, object)
        elif command == "fight":
            fight(room, object)
        else:
            print("I don't understand")

        if player['lives'] <= 0:
            print("You die!  Game over!")
            break

def stop():
    print("Bye")


if __name__ == "__main__":
    start()
    run()
    stop()