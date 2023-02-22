def get_stylish_format(data, indent=''):
    output = '{\n'
    for item in data:
        item_type = data[item].get('type')
        item_value = get_value(data[item].get('value'), indent)
        item_previus_value = get_value(data[item].get('previus_value'), indent)
        item_children = data[item].get('children')
        new_indent = indent + "    "
        if item_type == 'nested':
            children_value = get_stylish_format(item_children, new_indent)
            output += f'{new_indent}{item}: {children_value}\n'
        elif item_type == 'updated':
            output += f'{indent}  - {item}: {item_previus_value}\n'
            output += f'{indent}  + {item}: {item_value}\n'
        else:
            sign = types[item_type]
            output += f'{indent}  {sign} {item}: {item_value}\n'
    return output + indent + '}'


def get_value(value, indent):
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return get_stylish_dict(value, indent + '    ')
    if isinstance(value, bool):
        return str(value).lower()
    return value


def get_stylish_dict(item, indent=''):
    stylish_output = '{\n'
    new_indent = indent + "    "
    for key in item:
        item_value = item[key]
        if isinstance(item_value, dict):
            item_value = get_stylish_dict(item_value, new_indent)
            stylish_output += f'{new_indent}{key}: {item_value}\n'
        else:
            stylish_output += f'{new_indent}{key}: {item_value}\n'
    return stylish_output + indent + '}'


types = {
    'added': '+',
    'removed': '-',
    'unchanged': ' ',
    'updated': '',
    'nested': ' '
}
