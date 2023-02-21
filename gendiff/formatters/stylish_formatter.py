from gendiff.formatters.types import types


def get_stylish_format(data, ident=''):
    output = '{\n'
    for item in data:
        item_type = data[item].get('type')
        item_value = get_value(data[item].get('value'), ident)
        item_previus_value = get_value(data[item].get('previus_value'), ident)
        item_children = data[item].get('children')
        new_ident = ident + "    "
        if item_type == 'nested':
            children_value = get_stylish_format(item_children, new_ident)
            output += f'{new_ident}{item}: {children_value}\n'
        elif item_type == 'updated':
            output += f'{ident}  - {item}: {item_previus_value}\n'
            output += f'{ident}  + {item}: {item_value}\n'
        else:
            sign = types[item_type]
            output += f'{ident}  {sign} {item}: {item_value}\n'
    return output + ident + '}'


def get_value(value, ident):
    if isinstance(value, dict):
        return get_stylish_dict(value, ident + '    ')
    if isinstance(value, bool):
        return str(value).lower()
    return value


def get_stylish_dict(item, ident=''):
    stylish_output = '{\n'
    new_ident = ident + "    "
    for key in item:
        item_value = item[key]
        if isinstance(item_value, dict):
            item_value = get_stylish_dict(item_value, new_ident)
            stylish_output += f'{new_ident}{key}: {item_value}\n'
        else:
            stylish_output += f'{new_ident}{key}: {item_value}\n'
    return stylish_output + ident + '}'
