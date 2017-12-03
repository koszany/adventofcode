def get_checksum(file_name):
    checksum = 0

    f = open(file_name)
    for line in f:
        numbers = line.strip().split('\t')
        convert_list_string_to_int(numbers)
        checksum += max(numbers) - min(numbers)
    f.close()

    return checksum

def sum_evenly_divisible_values(file_name):
    checksum = 0

    f = open(file_name)
    for line in f:
        numbers = line.strip().split('\t')
        convert_list_string_to_int(numbers)
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] % numbers[j] == 0:
                    checksum += numbers[i]/numbers[j]
                if numbers[j] % numbers[i] == 0:
                    checksum += numbers[j]/numbers[i]
    f.close()

    return checksum

def convert_list_string_to_int(seq):
    for i in range(len(seq)):
        seq[i] = int(seq[i])


def main():
    print(get_checksum("puzzle_input.csv"))
    print(sum_evenly_divisible_values("puzzle_input.csv"))

if __name__ == '__main__':
    main()
