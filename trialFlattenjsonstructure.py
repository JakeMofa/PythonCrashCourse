def flattenjson(data, parentkey =, sep = '.'):
    items = {}

    for key, value in data.items():
        newkey = f{parentkey}{sep}{key} if parent_key else key
    
        if isinstance(value, dict):
            items.update(flattenjson(value, newkey, sep))
        else:
            items[newkey] = value
        
        return items