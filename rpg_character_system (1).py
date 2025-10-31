VALID_CLASSES = ["Warrior", "Mage", "Rogue", "Cleric"]

# Map many input variants to a canonical class name
_CLASS_CANON = {
    "warrior": "Warrior",
    "mage": "Mage",
    "rogue": "Rogue",
    "cleric": "Cleric",
}

def _canonical_class(name):
    if not isinstance(name, str):
        return None
    key = name.strip().casefold()
    return _CLASS_CANON.get(key)


def calculate_stats(char_class, level):
    """Return a tuple of (strength, magic, health) based on class and level.
    Returns None if class is invalid or level is not a number.
    """
    canon = _canonical_class(char_class)
    if canon is None:
        return None

    # Coerce level to int if possible (tests may pass ints; be permissive)
    try:
        lvl = int(level)
    except (TypeError, ValueError):
        return None
    if lvl < 1:
        lvl = 1  # clamp to minimum level 1

    if canon == "Warrior":
        strength = 10 + 3 * lvl
        magic = 2 + 1 * lvl
        health = 20 + 5 * lvl
    elif canon == "Mage":
        strength = 3 + 1 * lvl
        magic = 10 + 3 * lvl
        health = 12 + 4 * lvl
    elif canon == "Rogue":
        strength = 7 + 2 * lvl
        magic = 5 + 1 * lvl
        health = 15 + 3 * lvl
    elif canon == "Cleric":
        strength = 5 + 1 * lvl
        magic = 8 + 2 * lvl
        health = 18 + 4 * lvl
    else:
        return None

    return (strength, magic, health)


def create_character(name, char_class):
    """Return a character dictionary with initial stats or None on invalid input."""
    if not isinstance(name, str) or not name.strip():
        return None

    canon = _canonical_class(char_class)
    if canon is None:
        return None

    stats = calculate_stats(canon, 1)
    if stats is None:
        return None

    strength, magic, health = stats
    return {
        "name": name.strip(),
        "class": canon,
        "level": 1,
        "strength": strength,
        "magic": magic,
        "health": health,
    }


def save_character(character, filename):
    """Save character to a file in simple text format.
    Returns True on success, False on any error or invalid input.
    Format:
    name:<name>\n
    class:<class>\n
    level:<level>\n
    strength:<strength>\n
    magic:<magic>\n
    health:<health>\n
    """
    # Validate inputs
    if not isinstance(character, dict) or not isinstance(filename, str) or not filename:
        return False

    required_keys = ["name", "class", "level", "strength", "magic", "health"]
    for k in required_keys:
        if k not in character:
            return False

    # Build content
    try:
        content = (
            f"name:{character['name']}\n"
            f"class:{character['class']}\n"
            f"level:{int(character['level'])}\n"
            f"strength:{int(character['strength'])}\n"
            f"magic:{int(character['magic'])}\n"
            f"health:{int(character['health'])}\n"
        )
    except (KeyError, ValueError, TypeError):
        return False

    # Attempt to write
    try:
        with open(filename, "w") as f:
            f.write(content)
        return True
    except Exception:
        # Any OS/path/permissions errors translate to False (tests expect boolean)
        return False


def load_character(filename):
    """Load a character from a file and return the dictionary, or None on error."""
    if not isinstance(filename, str) or not filename:
        return None

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except Exception:
        return None

    data = {}
    for line in lines:
        parts = line.strip().split(":", 1)
        if len(parts) != 2:
            return None  # invalid format
        key, value = parts[0], parts[1]
        if key in ["level", "strength", "magic", "health"]:
            try:
                value = int(value)
            except ValueError:
                return None
        data[key] = value

    # Validate class
    canon = _canonical_class(data.get("class"))
    if canon is None:
        return None
    data["class"] = canon

    # Validate presence of all keys
    required_keys = ["name", "class", "level", "strength", "magic", "health"]
    if not all(k in data for k in required_keys):
        return None

    return data


def level_up(character):
    """Increase the character's level and recalculate stats. Return updated dict or None."""
    if not isinstance(character, dict):
        return None
    canon = _canonical_class(character.get("class"))
    if canon is None:
        return None

    try:
        character["level"] = int(character.get("level", 1)) + 1
    except (TypeError, ValueError):
        character["level"] = 2

    stats = calculate_stats(canon, character["level"])
    if stats is None:
        return None

    strength, magic, health = stats
    character["class"] = canon
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    return character


def display_character(character):
    """Display character info nicely (prints). No return."""
    if not isinstance(character, dict):
        return
    print(f"Name: {character.get('name')}")
    print(f"Class: {character.get('class')}")
    print(f"Level: {character.get('level')}")
    print(f"Strength: {character.get('strength')}")
    print(f"Magic: {character.get('magic')}")
    print(f"Health: {character.get('health')}")
