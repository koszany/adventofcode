def get_amount_unique_passphrases(file_name):
    passphrases_counter = 0
    with open(file_name) as f:
        for line in f:
            passphrase = line.strip().split(' ')
            if is_valid(passphrase):
                passphrases_counter += 1

    return passphrases_counter

def get_amount_passphrases_no_annagrams(file_name):
    passphrases_counter = 0
    with open(file_name) as f:
        for line in f:
            passphrase = line.strip().split(' ')
            if is_complex_of_no_annagram_words(passphrase):
                passphrases_counter += 1

    return passphrases_counter

def is_valid(passphrase):
    for i in range(len(passphrase)):
        for j in range(i+1, len(passphrase)):
            if passphrase[i] == passphrase[j]:
                return False
    return True

def is_complex_of_no_annagram_words(passphrase):
    for i in range(len(passphrase)-1, -1, -1):
        for j in range(i-1, -1, -1 ):
            if is_annagram(passphrase[i], passphrase[j]):
                return False
    return True

def is_annagram(word, pattern):
    if len(word) == len(pattern):
        for letter in word:
            if word.count(letter) != pattern.count(letter):
                return False
        return True
    else:
        return False

def main():
    print(get_amount_unique_passphrases('puzzle_input.csv'))
    print(get_amount_passphrases_no_annagrams('puzzle_input.csv'))

if __name__ == '__main__':
    main()
