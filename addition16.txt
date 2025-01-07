def write_json_file(filename, data):
    with open(filename, 'w') as config_file:
        json.dump(data, config_file)
