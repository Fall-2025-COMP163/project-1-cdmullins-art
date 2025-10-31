# project1_starter.py
# RPG Character Module – Autograder-Compatible Starter

# Character classes and modifiers
CLASS_MODIFIERS = {
    "Warrior": {"strength": 10, "magic": 2, "health": 20},
    "Mage": {"strength": 3, "magic": 10, "health": 12},
    "Rogue": {"strength": 7, "magic": 5, "health": 15},
    "Cleric": {"strength": 5, "magic": 8, "health": 18}
}

# Stat growth per level
GROWTH_RATES = {
    "Warrior": {"strength": 3, "magic": 1, "health": 5},
    "Mage": {"strength": 1, "magic": 3, "health": 4},
    "Rogue": {"strength": 2, "magic": 1, "health": 3},
    "Cleric": {"strength": 1, "magic": 2, "health": 4}
}

VALID_CLASSES = ["Warrior", "Mage", "Rogue", "Cleric"]


def calculate_stats(char_class, level):
    """Return a tuple (strength, magic, health) based on class and level"""
    char_class = char_class.capitalize()
    if char_class not in VALID_CLASSES:
        return None
    base = CLASS_MODIFIERS[char_class]
    growth = GROWTH_RATES[char_class]
    strength = base["strength"] + growth["strength"] * level
    magic = base["magic"] + growth["magic"] * level
    health = base["health"] + growth["health"] * level
    return (strength, magic, health)


def create_character(name, char_class):
    """Return character dictionary with initial stats"""
    char_class = char_class.capitalize()
    if char_class not in VALID_CLASSES:
        return None
    stats = calculate_stats(char_class, 1)
    return {
        "name": name,
        "class": char_class,
        "level": 1,
        "strength": stats[0],
        "magic": stats[1],
        "health": stats[2],
        "gold": 100,
        "equipment": []
    }


def save_character(character, filename):
    """Save character to file in required format; return True on success, False on error"""
    if character is None or not isinstance(filename, str) or filename == "":
        return False
    file = open(filename, "w")
    if file.closed:
        return False
    content = (
        f"name:{character['name']}\n"
        f"class:{character['class']}\n"
        f"level:{character['level']}\n"
        f"strength:{character['strength']}\n"
        f"magic:{character['magic']}\n"
        f"health:{character['health']}\n"
    )
    file.write(content)
    file.close()
    return True


def load_character(filename):
    """Load character from file and return dictionary; return None if file not found"""
    import os
    if not os.path.exists(filename):
        return None
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    data = {}
    for line in lines:
        if ":" not in line:
            continue
        key, value = line.strip().split(":", 1)
        if key in ["level", "strength", "magic", "health"]:
            data[key] = int(value)
        else:
            data[key] = value
    return data


def level_up(character):
    """Increase character level and recalc stats"""
    if character is None or "class" not in character or character["class"] not in VALID_CLASSES:
        return character
    character["level"] += 1
    stats = calculate_stats(character["class"], character["level"])
    character["strength"] = stats[0]
    character["magic"] = stats[1]
    character["health"] = stats[2]
    character["gold"] += 50
    return character


def display_character(character):
    """Display character info nicely"""
    if character is None:
        print("No character to display")
        return
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character.get('gold', 0)}")
    print(f"Equipment: {character.get('equipment', [])}")
