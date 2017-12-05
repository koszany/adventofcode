def get_amount_valid_passphrases(file_name):

    passphrases_counter = 0
    with open(file_name) as f:
        for line in f:
            passphrase = line.strip().split(' ')
            if is_valid(passphrase):
                passphrases_counter += 1

    return passphrases_counter

def is_valid(passphrase):
    for i in range(len(passphrase)):
        for j in range(i+1, len(passphrase)):
            if passphrase[i] == passphrase[j]:
                return False
    return True

def main():
    print(get_amount_valid_passphrases('puzzle_input.csv'))

if __name__ == '__main__':
    main()
