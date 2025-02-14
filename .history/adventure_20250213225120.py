"""Week 4 Coding Assignment
The inventory and the Dungeon of Choices
Made by Andreas Marangos"""

import random

def display_player_status(player_health):
    """Display the player's current health"""
    print(f"Your current health: {player_health}")

def handle_path_choice(player_health):
    """Randomly choose a path for the player
    takes the player health and then outputs the new player health"""
    path = random.choice(["left", "right"])

    if path == "left":
        print("You encounter a friendly gnome who heals you for 10 health points.")
        player_health = min(player_health + 10, 100)
    else:
        print("You fall into a pit and lose 15 health points.")
        player_health -= 15
        if player_health < 0:
            player_health = 0
            print("You are barely alive!")

    return player_health

def player_attack(monster_health):
    """Randomly determine if the player lands a critical hit
    takes the monster health and then outputs the new monster health"""
    damage = 15
    monster_health -= damage
    print(f"You strike the monster for {damage} damage!")
    return monster_health

def monster_attack(player_health):
    """Randomly determine if the monster lands a critical hit
    takes the player health and then outputs the new player"""
    if random.random() < 0.5:
        damage = 20
        print("The monster lands a critical hit for 20 damage!")
    else:
        damage = 10
        print("The monster hits you for 10 damage!")

    player_health -= damage
    return player_health

def combat_encounter(player_health, monster_health, has_treasure):
    """Combat loop
    takes the player health, monster health and has treasure
    and then outputs if the player has the treasure"""
    print("A monster appears! Prepare for battle!")

    while player_health > 0 and monster_health > 0:
        print(f"Your Health: {player_health} | Monster's Health: {monster_health}")

        monster_health = player_attack(monster_health)
        if monster_health <= 0:
            print("You defeated the monster!")
            return has_treasure

        player_health = monster_attack(player_health)
        if player_health <= 0:
            print("You have been defeated!")
            return False

def check_for_treasure(has_treasure):
    """Check if the player found the treasure
    takes the has treasure and then outputs if the player has the treasure"""
    if has_treasure:
        print("You found the hidden treasure! You win!")
    else:
        print("The monster did not have the treasure. You continue your journey.")


def acquire_item(inventory, item):
    """Add an item to the player's inventory"""
    inventory.append(item)
    # used append to add the item to the inventory list
    # used append because it is to add one item at a time
    print(f"You acquired a {item}!")

def display_inventory(inventory):
    """Display the player's inventory"""
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for i, item in enumerate(inventory):
            print(f"{i+1}. {item}")

def enter_dungeon(player_health, inventory, dungeon_rooms):
    """This section goes through the tuple of dungeon rooms and then outputs the player health and inventory"""
    for room_description, item, challenge_type, challenge_outcome in dungeon_rooms:
        print(room_description)

        if item:
            print(f"You found a {item}!")
            acquire_item(inventory, item)

        if challenge_type == "puzzle":
            print("You encounter a puzzle!")
            choice = input("Do you want to 'solve' or 'skip' the puzzle? ").lower()

            if choice == "solve":
                success = random.choice([True, False])
                if success:
                    print(challenge_outcome[0])  # Success message
                else:
                    print(challenge_outcome[1])  # Failure message
                player_health += challenge_outcome[2]  # Health change

        elif challenge_type == "trap":
            print("You see a potential trap!")
            choice = input("Do you want to 'disarm' or 'bypass' the trap? ").lower()

            if choice == "disarm":
                success = random.choice([True, False])
                if success:
                    print(challenge_outcome[0])  # Success message
                else:
                    print(challenge_outcome[1])  # Failure message
                player_health += challenge_outcome[2]  # Health change

        elif challenge_type == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")

        if player_health <= 0:
            player_health = 0
            print("You are barely alive!")

        display_inventory(inventory)

    print(f"You exited the dungeon with {player_health} health.")
    return player_health, inventory

def main():
    """Main game loop"""
    dungeon_rooms = [
    ("A dusty old library", "key", "puzzle", ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
    ("A narrow passage with a creaky floor", None, "trap", ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
    ("A grand hall with a shimmering pool", "healing potion", "none", None),
    ("A small room with a locked chest", "treasure", "puzzle", ("You cracked the code!", "The chest remains stubbornly locked.", -5))
]
    player_health = 100
    monster_health = 70
    inventory = []
    has_treasure = random.choice([True, False])

    display_player_status(player_health)

    player_health = handle_path_choice(player_health)

    if player_health > 0:  # Only proceed if still alive
        treasure_obtained_in_combat = combat_encounter(player_health, monster_health, has_treasure)
        check_for_treasure(treasure_obtained_in_combat)

if __name__ == "__main__":
    """Run the game"""
    main()
