def flatten_json(data, parent_key="", sep="."):
    items = {}

    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key

        if isinstance(value, dict):
            items.update(flatten_json(value, new_key, sep))
        else:
            items[new_key] = value

    return items

