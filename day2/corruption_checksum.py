def get_checksum(file_name):
    checksum = 0

    f = open(file_name)
    for line in f:
        numbers = line.split('\t')
        convert_list_string_to_int(numbers)
        checksum += max(numbers) - min(numbers)
    f.close()

    return checksum

def convert_list_string_to_int(seq):
    for i in range(len(seq)):
        seq[i] = int(seq[i])


def main():
    print(get_checksum("puzzle_input.csv"))

if __name__ == '__main__':
    main()
