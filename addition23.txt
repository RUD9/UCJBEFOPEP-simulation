def wait_for_signal():
    while True:
        time.sleep(0.1)
        if read_json('config_filename9.json') == "1":
            write_json('config_filename9.json', '0')
            break
