
import json
import time
import datetime


def read_json_file(filename):
    with open(filename, 'r') as config_file:
        return json.load(config_file)


def write_json_file(filename, data):
    with open(filename, 'w') as config_file:
        json.dump(data, config_file)


def wait_for_signal(signal_file):
    while True:
        time.sleep(0.1)
        if read_json_file(signal_file) == "1":
            write_json_file(signal_file, '0')
            break


def process_input(message):
    for char in message:
        wait_for_signal('config_filename4.json')

        R1 = read_json_file('config_filename5.json')[1:2]
        print(R1)

        status = '1' if R1 == char else '0'
        write_json_file('config_filename3.json', status)
        write_json_file('config_filename9.json', '1')


def process_sequence(length):
    for _ in range(length):
        wait_for_signal('config_filename4.json')

        R1 = read_json_file('config_filename5.json')[1:2]
        write_json_file('config_filename3.json', str(1 - int(R1)))
        write_json_file('config_filename9.json', '1')


def process_password(passw):
    for digit in str(passw):
        wait_for_signal('config_filename4.json')

        R1 = read_json_file('config_filename5.json')[1:2]
        print(R1)

        status = '1' if R1 == digit else '0'
        write_json_file('config_filename3.json', status)
        write_json_file('config_filename9.json', '1')


def main():
    print(datetime.datetime.now())

    message = list(input())
    passw = 101001

    if message:
        process_input(message)

    process_sequence(8)
    process_password(passw)

    print(datetime.datetime.now())


if __name__ == "__main__":
    while True:
        main()

