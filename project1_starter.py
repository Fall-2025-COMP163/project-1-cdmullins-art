"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function, It helped streamline syntax, debug errors, and optimize algorithms.
Additionally, AI provided insights into best practices, assisted with logic troubleshooting, and suggested improvements, significantly speeding up development and enhancing code efficiency.
"""

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """

    level = 1
    health, magic, strength = calculate_stats(character_class, level)

    gold = 1000

    character = {
        "name" : name,
        "class" : character_class,
        "level" : level,
        "strength" : strength,
        "magic" : magic,
        "health" : health,
        "gold" : gold

    {
    return character
    

    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    if character_class.lower() == "warrior":
        strength = 10 + (level * 5)
        magic = 2 + (level * 1)
        health = 120 + (level * 15)
    elif character_class.lower() == "mage":
        strength = 8 + (level * 2)
        magic = 15 + (level * 4)
        health = 135 + (level * 8)
    elif character_class.lower() == "rogue":
        strength = 15 + (level * 10)
        magic = 7 + (level * 3)
        health = 135 + (level * 5)
    elif character_class.lower() == "cleric":
        strength = 8 + (level * 12)
        magic = 7 + (level * 6)
        health = 150 + (level * 9)
    else:
        strength = 5 + (level * 2)
        magic = 5 + (level * 2)
        health = 50 + (level * 2)
    retutn ( strength, magic, health)

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    """
    if filename == "":
        return False

    import os
    directory = os.path.dirname(filename)

    if directory != "" and not os.path.exists(directory):
        return False


    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")

    return True


def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    import os
    if not os.path.exists(filename):
        return None

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    data = {}
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(":", 1)
            data[key] = value


    character = {
        "name": data.get("Character Name", ""),
        "class": data.get("Class", ""),
        "level": int(data.get("Level", "1")),
        "strength": int(data.get("Strength", "0")),
        "magic": int(data.get("Magic", "0")),
        "health": int(data.get("Health", "0")),
        "gold": int(data.get("Gold", "0")),


    }

    return character

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    """

    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    
def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    character["level"] += 1
    health, strength, magic = calculate_stats(character["class"], character["level"])
    character["health"] = health
    chracter["strength"] = strength
    character["magic"] = magic

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    char = create_character("Reacher", "Cleric")
    display_character(char)

    print("\nSaving character...")
    save_character(char, "reacher.txt")

    print("\nLoading character...")
    loaded = load_character("reacher.txt")
    display_character(loaded)

    print("\nLeveling up character...")
    level_up(loaded)
    display_character(loaded)
  
