def process_sequence(length):
    for _ in range(length):
        wait_for_signal('config_filename4.json')

        R1 = read_json_file('config_filename5.json')[1:2]
        write_json_file('config_filename3.json', str(1 - int(R1)))
        write_json_file('config_filename9.json', '1')
