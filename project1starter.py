import os

# -------------------------------
# Function: calculate_stats
# -------------------------------
def calculate_stats(character_class, level):
    character_class = character_class.lower()
    if character_class == "warrior":
        strength = 10 + (level * 5)
        magic = 2 + (level * 1)
        health = 120 + (level * 10)
    elif character_class == "mage":
        strength = 3 + (level * 1)
        magic = 12 + (level * 5)
        health = 80 + (level * 8)
    elif character_class == "rogue":
        strength = 7 + (level * 3)
        magic = 6 + (level * 2)
        health = 70 + (level * 6)
    elif character_class == "cleric":
        strength = 6 + (level * 2)
        magic = 10 + (level * 4)
        health = 100 + (level * 9)
    else:
        raise ValueError("Invalid character class")
    return {"strength": strength, "magic": magic, "health": health}

# -------------------------------
# Function: create_character
# -------------------------------
def create_character(name, character_class):
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "gold": 100
    }
    stats = calculate_stats(character_class, character["level"])
    character.update(stats)
    return character

# -------------------------------
# Function: save_character
# -------------------------------
def save_character(character, filename):
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
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

# -------------------------------
# Function: level_up
# -------------------------------
def level_up(character):
    character["level"] += 1
    new_stats = calculate_stats(character["class"], character["level"])
    character.update(new_stats)
    print(f"{character['name']} leveled up to Level {character['level']}!")
    return character

# -------------------------------
# Main program (for testing)
# -------------------------------
if __name__ == "__main__":
    print("🎮 Welcome to the RPG Character Creator!\n")

    name = input("Enter your character's name: ").strip()
    character_class = input("Choose a class (Warrior, Mage, Rogue, Cleric): ").strip()

    character = create_character(name, character_class)
    display_character(character)

    # Save character
    save_file = f"{name}_save.txt"
    save_character(character, save_file)
    print(f"\nCharacter saved to {save_file}.")

    # Simulate level up
    character = level_up(character)
    display_character(character)

    # Save again after leveling up
    save_character(character, save_file)
    print(f"\nUpdated character saved to {save_file}.")
