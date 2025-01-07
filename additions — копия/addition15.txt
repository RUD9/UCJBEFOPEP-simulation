def read_json_file(filename):
    with open(filename, 'r') as config_file:
        return json.load(config_file)
