def get_plain_format(data, parent_property=''):
    output = ''
    for item in data:
        property_path = parent_property + item
        item_type = data[item].get('type')
        item_value = get_value(data[item].get('value'))
        item_previus_value = get_value(data[item].get('previus_value'))
        item_children = data[item].get('children')
        if item_type == 'nested':
            get_plain_format(item_children, property_path + '.')
            nested_value = get_plain_format(item_children, property_path + '.')
            output += f"{nested_value}\n"
        elif item_type == 'updated':
            output += f"Property '{property_path}' was {item_type}."
            output += f" From {item_previus_value} to {item_value}\n"
        elif item_type == 'added':
            output += f"Property '{property_path}' was {item_type} "
            output += f"with value: {item_value}\n"
        elif item_type == 'removed':
            output += f"Property '{property_path}' was {item_type}\n"
    return output.rstrip()


def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    return f"'{value}'"
