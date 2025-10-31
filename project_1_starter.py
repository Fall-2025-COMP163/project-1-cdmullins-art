import os

# -------------------------------
# Function: calculate_stats
# -------------------------------
def calculate_stats(character_class, level):
    cls = character_class.lower()
    if cls == "warrior":
        strength = 10 + (level * 5)
        magic = 2 + (level * 1)
        health = 120 + (level * 10)
    elif cls == "mage":
        strength = 3 + (level * 1)
        magic = 12 + (level * 5)
        health = 80 + (level * 8)
    elif cls == "rogue":
        strength = 7 + (level * 3)
        magic = 6 + (level * 2)
        health = 70 + (level * 6)
    elif cls == "cleric":
        strength = 6 + (level * 2)
        magic = 10 + (level * 4)
        health = 100 + (level * 9)
    else:
        raise ValueError("Invalid character class")
    return (strength, magic, health)

# -------------------------------
# Function: create_character
# -------------------------------
def create_character(name, character_class):
    strength, magic, health = calculate_stats(character_class, 1)
    return {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }

# -------------------------------
# Function: save_character
# -------------------------------
def save_character(character, filename):
    if not character or not filename:
        return False
    if "/" in filename:
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            return False
    try:
        f = open(filename, "w")
        f.write(f"Character Name: {character['name']}\n")
        f.write(f"Class: {character['class']}\n")
        f.write(f"Level: {character['level']}\n")
        f.write(f"Strength: {character['strength']}\n")
        f.write(f"Magic: {character['magic']}\n")
        f.write(f"Health: {character['health']}\n")
        f.write(f"Gold: {character['gold']}\n")
        f.close()
        return True
    except:
        return False

# -------------------------------
# Function: load_character
# -------------------------------
def load_character(filename):
    if not os.path.exists(filename):
        return None
    character = {}
    f = open(filename, "r")
    for line in f:
        key, value = line.strip().split(": ")
        if key == "Character Name":
            character["name"] = value
        elif key == "Class":
            character["class"] = value
        elif key == "Level":
            character["level"] = int(value)
        elif key == "Strength":
            character["strength"] = int(value)
        elif key == "Magic":
            character["magic"] = int(value)
        elif key == "Health":
            character["health"] = int(value)
        elif key == "Gold":
            character["gold"] = int(value)
    f.close()
    return character

# -------------------------------
# Function: display_character
# -------------------------------
def display_character(character):
    print(f"=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    return None

# -------------------------------
# Function: level_up
# -------------------------------
def level_up(character):
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    return character

# -------------------------------
# Optional main program
# -------------------------------
if __name__ == "__main__":
    pass
