def is_nested(data):
    return isinstance(data, (dict, tuple, list, set))


def get_compared_data(first_data, second_data):
    compared_data = {}
    all_keys = list(first_data) + list(second_data)
    for key in sorted(all_keys):
        if is_nested(first_data.get(key)) and is_nested(second_data.get(key)):
            children = get_compared_data(first_data[key], second_data[key])
            compared_data[key] = {
                'type': 'nested',
                'children': children}
        elif key not in second_data:
            compared_data[key] = {
                'type': 'removed',
                'value': first_data[key]}
        elif key not in first_data:
            compared_data[key] = {
                'type': 'added',
                'value': second_data[key]}
        elif first_data[key] == second_data[key]:
            compared_data[key] = {
                'type': 'unchanged',
                'value': first_data[key]}
        else:
            compared_data[key] = {
                'type': 'updated',
                'value': second_data[key],
                'previus_value': first_data[key]}
    return compared_data
