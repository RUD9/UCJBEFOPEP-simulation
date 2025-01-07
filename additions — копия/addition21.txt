def read_json(filename):
    with open(filename, 'r') as config_file:
        return json.load(config_file)
