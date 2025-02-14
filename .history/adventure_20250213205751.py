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

def main():
    # Main game loop
    player_health = 100
    monster_health = 70
    has_treasure = random.choice([True, False])

    display_player_status(player_health)

    player_health = handle_path_choice(player_health)

    if player_health > 0:  # Only proceed if still alive
        treasure_obtained_in_combat = combat_encounter(player_health, monster_health, has_treasure)
        check_for_treasure(treasure_obtained_in_combat)

if __name__ == "__main__":
    # Run the game
    main()
