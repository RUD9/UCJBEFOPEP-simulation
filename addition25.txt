elif sc == "password":
    for digit in passw:
        wait_for_signal()

        c = read_json('config_filename3.json')
        data_loaded = read_json('config_filename11.json')
        R2 = data_loaded[1:2]

        if (c == '0' and int(digit) != int(R2)) or \
                (c == '1' and int(digit) != (1 - int(R2))):
            sc = "sd"
            break

    t += 1
    if t >= 4:
        sc = "s"
        t = 0
