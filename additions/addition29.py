import time
import json
global rezalt
global rez


def read_json(filename):
    with open(filename, 'r') as config_file:
        return json.load(config_file)


def write_json(filename, data):
    with open(filename, 'w') as config_file:
        json.dump(data, config_file)


def wait_for_signal():
    while True:
        time.sleep(0.1)
        if read_json('config_filename9.json') == "1":
            write_json('config_filename9.json', '0')
            break


def main():
    rez = []
    rezalt = []
    passw = "101001"
    sc = "s"
    t = 0

    while True:
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

        elif sc == "sd":
            print('sd')
            break


if __name__ == "__main__":
    main()

