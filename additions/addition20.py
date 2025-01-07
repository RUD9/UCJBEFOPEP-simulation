def process_password(passw):
    for digit in str(passw):
        wait_for_signal('config_filename4.json')

        R1 = read_json_file('config_filename5.json')[1:2]
        print(R1)

        status = '1' if R1 == digit else '0'
        write_json_file('config_filename3.json', status)
        write_json_file('config_filename9.json', '1')
