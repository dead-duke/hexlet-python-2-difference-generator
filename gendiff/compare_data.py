def compare_data(first_data, second_data):
    compared_data = {}
    all_keys = list(first_data) + list(second_data)
    for key in sorted(all_keys):
        if key not in second_data:
            compared_data[key] = {
                'value': first_data[key],
                'type': 'removed'}
        elif key not in first_data:
            compared_data[key] = {
                'value': second_data[key],
                'type': 'added'}
        elif first_data[key] == second_data[key]:
            compared_data[key] = {
                'value': first_data[key],
                'type': 'unchanged'}
        else:
            compared_data[key] = {
                'previus_value': first_data[key],
                'value': second_data[key],
                'type': 'changed'}
    return compared_data
