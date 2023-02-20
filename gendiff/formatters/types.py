types = {
    'added': '+',
    'removed': '-',
    'unchanged': ' ',
    'changed': ''
}


def get_value(value):
    if type(value) is bool:
        return str(value).lower()
    return value
