# project1_starter.py

VALID_CLASSES = ["Warrior", "Mage", "Rogue", "Cleric"]

CLASS_MODIFIERS = {
    "Warrior": {"strength": 10, "magic": 2, "health": 20, "growth": {"strength":3, "magic":1, "health":5}},
    "Mage":    {"strength": 3,  "magic":10, "health":12, "growth": {"strength":1, "magic":3, "health":4}},
    "Rogue":   {"strength": 7,  "magic": 5, "health":15, "growth": {"strength":2, "magic":1, "health":3}},
    "Cleric":  {"strength": 5,  "magic": 8, "health":18, "growth": {"strength":1, "magic":2, "health":4}}
}

def calculate_stats(char_class, level):
    if char_class not in VALID_CLASSES:
        return None
    base = CLASS_MODIFIERS[char_class]
    strength = base["strength"] + level * base["growth"]["strength"]
    magic = base["magic"] + level * base["growth"]["magic"]
    health = base["health"] + level * base["growth"]["health"]
    return (strength, magic, health)

def create_character(name, char_class):
    if char_class not in VALID_CLASSES or not name:
        return None
    stats = calculate_stats(char_class, 1)
    return {
        "name": name,
        "class": char_class,
        "level": 1,
        "strength": stats[0],
        "magic": stats[1],
        "health": stats[2]
    }

def save_character(character, filename):
    if character is None or not isinstance(filename, str) or filename == "":
        return False
    import os
    dir_name = os.path.dirname(filename)
    if dir_name != "" and not os.path.exists(dir_name):
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
    import os
    if not os.path.exists(filename) or not isinstance(filename, str) or filename == "":
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
            if value.isdigit():
                data[key] = int(value)
            else:
                return None
        else:
            data[key] = value
    return data

def level_up(character):
    if character is None or "class" not in character:
        return None
    character["level"] += 1
    stats = calculate_stats(character["class"], character["level"])
    character["strength"], character["magic"], character["health"] = stats
    return character

def display_character(character):
    if character is None:
        return
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
