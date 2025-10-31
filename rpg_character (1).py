
def calculate_stats(char_class, level):
    """Return a tuple of (strength, magic, health) based on class and level"""
    char_class = char_class.capitalize()  # normalize input
    if char_class == "Warrior":
        strength = 10 + 3 * level
        magic = 2 + 1 * level
        health = 20 + 5 * level
    elif char_class == "Mage":
        strength = 3 + 1 * level
        magic = 10 + 3 * level
        health = 12 + 4 * level
    elif char_class == "Rogue":
        strength = 7 + 2 * level
        magic = 5 + 1 * level
        health = 15 + 3 * level
    elif char_class == "Cleric":
        strength = 5 + 1 * level
        magic = 8 + 2 * level
        health = 18 + 4 * level
    else:
        return None
    return (strength, magic, health)


def create_character(name, char_class):
    """Return a character dictionary with initial stats"""
    stats = calculate_stats(char_class, 1)
    if stats is None:
        return None
    strength, magic, health = stats
    return {
        "name": name,
        "class": char_class.capitalize(),
        "level": 1,
        "strength": strength,
        "magic": magic,
        "health": health
    }


def save_character(character, filename):
    """Save character to a file in simple text format and return True if successful"""
    if character is None or not isinstance(filename, str) or filename == "":
        return False

    content = (
        f"name:{character['name']}\n"
        f"class:{character['class']}\n"
        f"level:{character['level']}\n"
        f"strength:{character['strength']}\n"
        f"magic:{character['magic']}\n"
        f"health:{character['health']}\n"
    )

    with open(filename, "w") as file:
        file.write(content)

    return True


def load_character(filename):
    """Load a character from a file and return the dictionary"""
    with open(filename, "r") as file:
        lines = file.readlines()

    data = {}
    for line in lines:
        key, value = line.strip().split(":")
        if key in ["level", "strength", "magic", "health"]:
            value = int(value)
        data[key] = value
    return data


def level_up(character):
    """Increase the character's level and recalculate stats"""
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    return character


def display_character(character):
    """Display character info nicely"""
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
