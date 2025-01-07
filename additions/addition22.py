def write_json(filename, data):
    with open(filename, 'w') as config_file:
        json.dump(data, config_file)
