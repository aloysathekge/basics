def inventory(items: list) -> dict:
    """
    Updates the inventory based on the given list of operations.

    Args:
        items (list): A list of tuples containing the operation and item name.

    Returns:
        dict: The updated inventory.

    Raises:
        ValueError: If an invalid operation is encountered or if an item is removed that does not exist in the inventory.
    """
    result = {}
    for item in items:
        operation, name = item

        newName = name.lower()
        if operation == "add":
            result[newName] = result.get(newName, 0) + 1
        elif operation == "remove" and newName not in result:
            raise ValueError(f"item does not {newName} in inventory")
        elif operation == "remove":
            result[newName] = result.get(newName, 0) - 1

        elif operation not in ["add", "remove"]:
            raise ValueError(f"invalid operation {operation}")

    return result


input = [
    ("add", "apple"),
    ("remove", "apple"),
    ("add", "BanaNa"),
    ("add", "bananA"),
    ("add", "mango"),
]
print(inventory(input))

# Notes
