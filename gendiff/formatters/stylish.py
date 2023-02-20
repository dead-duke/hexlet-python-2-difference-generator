from gendiff.formatters.types import types, get_value


def get_stylish_format(data):
    stylish_output = '{\n'
    for item in data:
        item_type = data[item]['type']
        item_sign = types[item_type]
        item_value = get_value(data[item]['value'])
        if item_type == 'changed':
            item_previus_value = get_value(data[item]['previus_value'])
            stylish_output += f'  - {item}: {item_previus_value}\n'
            stylish_output += f'  + {item}: {item_value}\n'
        else:
            stylish_output += f'  {item_sign} {item}: {item_value}\n'
    return stylish_output + '}'
