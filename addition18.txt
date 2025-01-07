def process_input(message):
    for char in message:
        wait_for_signal('config_filename4.json')

        R1 = read_json_file('config_filename5.json')[1:2]
        print(R1)

        status = '1' if R1 == char else '0'
        write_json_file('config_filename3.json', status)
        write_json_file('config_filename9.json', '1')
