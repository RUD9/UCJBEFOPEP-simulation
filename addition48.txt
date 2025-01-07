def main():
    print(datetime.datetime.now())
    message = list(input())
    passw = 101001
    if message:
        process_input(message, passw)
    process_sequence(8)
    process_password(passw)
    print(datetime.datetime.now())
