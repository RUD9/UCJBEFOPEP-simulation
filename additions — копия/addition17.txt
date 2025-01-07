def wait_for_signal(signal_file):
    while True:
        time.sleep(0.1)
        if read_json_file(signal_file) == "1":
            write_json_file(signal_file, '0')
            break
