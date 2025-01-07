if sc == "s":
    wait_for_signal()

    c = read_json('config_filename3.json')
    data_loaded = read_json('config_filename11.json')

    R2 = data_loaded[1:2]

    rez.append(R2 if c == '0' else 1 - int(R2))
    print(rez)

    if len(rez) == 8:
        if sum(map(int, rez)) == 0:
            sc = "password"
        else:
            rezalt.append(rez)
            print(rezalt)
            rez = []
