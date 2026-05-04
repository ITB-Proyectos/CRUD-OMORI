import time

# Diccionary

main_character = "Main character"
special_character = "Special character"

characters = {
    "omori": {
        "name": "Omori",
        "lvl": 1,
        "health": 33,
        "juice": 20,
        "attack": 1,
        "type": main_character,
        "image": "https://static.wikia.nocookie.net/omori/images/8/89/Omori_Neutral_%28No_Background%29.gif/revision/latest?cb=20211217073238"
    },
    "kel": {
        "name": "Kel",
        "health": 130,
        "juice": 100,
        "lvl": 1,
        "attack": 1,
        "type": main_character,
        "image": "https://static.wikia.nocookie.net/omori/images/f/f4/DW_Kel_Neutral_%28No_Background%29.gif/revision/latest?cb=20210825074249"
    },
    "aubrey": {
        "name": "Aubrey",
        "health": 240,
        "juice": 25,
        "lvl": 1,
        "attack": 1,
        "type": main_character,
        "image": "https://static.wikia.nocookie.net/omori/images/a/ab/DW_Aubrey_Neutral_%28No_Background%29.gif/revision/latest?cb=20210825052349"
    },
    "hero": {
        "name": "Hero",
        "health": 260,
        "juice": 60,
        "lvl": 1,
        "attack": 1,
        "type": main_character,
        "image": "https://static.wikia.nocookie.net/omori/images/2/2b/DW_Hero_Neutral_%28No_Background%29.gif/revision/latest?cb=20210825075857"
    },
    "basil": {
        "name": "Basil",
        "health": 33,
        "juice": 20,
        "lvl": 1,
        "attack": 1,
        "type": special_character
    },
    "something": {
        "name": "Something",
        "health": 33,
        "juice": 20,
        "lvl": 1,
        "attack": 1,
        "type": special_character
    }
}

def add_omori(characters, name):
    input_name = input("Enter the character's name: ")
    input_health = int(input("Enter the character's health: "))
    input_juice = int(input("Enter the character's juice: "))
    input_attack = int(input("Enter the character's attack: "))
    input_type = input("Enter the character's type (main character/special character): ")
    if input_type.capitalize() in main_character:
        def_type = main_character
    elif input_type.capitalize() in special_character:
        def_type = special_character
    else:
        print("Invalid type. Defaulting to 'main character'.")
        def_type = main_character

    characters[input_name.lower()] = {
        "name": input_name.capitalize(),
        "health": input_health,
        "juice": input_juice,
        "lvl": 1,
        "attack": input_attack,
        "type": def_type
    }

    return characters
def search_omori(characters):
    input_name = input("Enter the character's name to search: ")
    if input_name.lower() in characters:
        character = characters[input_name.lower()]
        print("")
        print(f"Name: {character['name']}")
        print(f"Health: {character['health']}")
        print(f"Juice: {character['juice']}")
        print(f"Level: {character['lvl']}")
        print(f"Attack: {character['attack']}")
        print(f"Type: {character['type']}")
        print("")
    else:
        print("Character not found.")
    return characters

def list_omori(characters):
    for character in characters.values():
        print("")
        print(f"Name: {character['name']}")
        print(f"Health: {character['health']}")
        print(f"Juice: {character['juice']}")
        print(f"Level: {character['lvl']}")
        print(f"Attack: {character['attack']}")
        print(f"Type: {character['type']}")
        print("")
    return characters

def filter_omori(characters):
    print("Filter by stats:")
    input_health_filter = input("Health (leave blank to skip): ")
    input_juice_filter = input("Juice (leave blank to skip): ")
    input_lvl_filter = input("Level (leave blank to skip): ")
    input_attack_filter = input("Attack (leave blank to skip): ")
    input_type_filter = input("Type (main character (1) or special character (2)): ")

    for character in characters.values():
        if (not input_health_filter or character['health'] == int(input_health_filter)) and \
           (not input_juice_filter or character['juice'] == int(input_juice_filter)) and \
           (not input_lvl_filter or character['lvl'] == int(input_lvl_filter)) and \
           (not input_attack_filter or character['attack'] == int(input_attack_filter)) and \
           (not input_type_filter or character['type'].lower() == ("main character" if input_type_filter == "1" else "special character")):
            print("")
            print(f"Name: {character['name']}")
            print(f"Health: {character['health']}")
            print(f"Juice: {character['juice']}")
            print(f"Level: {character['lvl']}")
            print(f"Attack: {character['attack']}")
            print(f"Type: {character['type']}")
            print("")
    return characters

def remove_omori(characters, name):
    if name.lower() in characters:
        del characters[name.lower()]
        print("")
        print("Character removed successfully.")
        print("")
    else:
        print("Character not found.")
        print("")
    return characters

def show_stats(characters, name):
    if name.lower() in characters:
        character = characters[name.lower()]
        print("")
        print(f"Name: {character['name']}")
        print(f"Health: {character['health']}")
        print(f"Juice: {character['juice']}")
        print(f"Level: {character['lvl']}")
        print(f"Attack: {character['attack']}")
        print(f"Type: {character['type']}")
        print("")
    else:
        print("Character not found.")

def modify_stats(characters, name):
    if name.lower() in characters:
        character = characters[name.lower()]
        print("Enter new stats (leave blank to keep current value):")
        input_health = input(f"Health ({character['health']}): ")
        input_juice = input(f"Juice ({character['juice']}): ")
        input_lvl = input(f"Level ({character['lvl']}): ")
        input_attack = input(f"Attack ({character['attack']}): ")

        if input_health:
            character['health'] = int(input_health)
        if input_juice:
            character['juice'] = int(input_juice)
        if input_lvl:
            character['lvl'] = int(input_lvl)
        if input_attack:
            character['attack'] = int(input_attack)

        characters[name.lower()] = character
    else:
        print("Character not found.")

def character_with_highest_stat(characters, stat):
    print("For which stat do you want to find the character with the highest value?")
    print("1. Health")
    print("2. Juice")
    print("3. Level")
    print("4. Attack")
    print("5. Type")
    stat_choice = input("Select an option: ")

    if stat_choice == "1":
        stat = "health"
    elif stat_choice == "2":
        stat = "juice"
    elif stat_choice == "3":
        stat = "lvl"
    elif stat_choice == "4":
        stat = "attack"
    elif stat_choice == "5":
        stat = "type"
    else:
        print("Opción no válida.")
        return

    highest_character = None
    highest_value = -1

    for character in characters.values():
        if character[stat] > highest_value:
            highest_value = character[stat]
            highest_character = character

    if highest_character:
        print(f"Character with the highest {stat}:")
        print(f"Name: {highest_character['name']}")
        print(f"Health: {highest_character['health']}")
        print(f"Juice: {highest_character['juice']}")
        print(f"Level: {highest_character['lvl']}")
        print(f"Attack: {highest_character['attack']}")
        print(f"Type: {highest_character['type']}")
    else:
        print("No characters found.")

op = 99

while op != 0:
    print("================MENU================")
    print("1. Add character")
    print("2. Search character")
    print("3. List characters (ALL)")
    print("4. Search character (filter by stats)")
    print("5. Remove character")
    print("6. Show character stats")
    print("7. Modify character stats")
    print("0. Exit")
    print("====================================")

    op = int(input("Enter an option: "))

    if op == 1:
        name = input("Enter the character's variable name: ")
        characters = add_omori(characters, name.lower())
    elif op == 2:
        characters = search_omori(characters)
        input("Press 'Enter' to continue...")
    elif op == 3:
        list_omori(characters)
        input("Press 'Enter' to continue...")
    elif op == 4:
        characters = filter_omori(characters)
        input("Press 'Enter' to continue...")
    elif op == 5:
        name = input("Enter the name of the character to remove: ")
        characters = remove_omori(characters, name.lower())
        input("Press 'Enter' to continue...")
    elif op == 6:
        name = input("Enter the name of the character to show stats: ")
        show_stats(characters, name.lower())
        input("Press 'Enter' to continue...")
    elif op == 7:
        name = input("Enter the name of the character to modify stats: ")
        modify_stats(characters, name.lower())
        input("Press 'Enter' to continue...")
    elif op == 0:
        print("Exiting the program...")
    else:
        print("Invalid option. Please enter a valid option.")