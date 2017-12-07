def main():
    banks = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]
    configs = []
    steps = 0

    while not is_sequence_repeated(banks, configs):
        configs.append(banks[:])
        index_max = banks.index(max(banks))

        amout_blocks = banks[index_max]
        banks[index_max] = 0

        index = index_max
        while amout_blocks > 0:
            if index < len(banks)-1:
                index += 1
            else:
                index = 0
            banks[index] += 1
            amout_blocks -= 1

        steps += 1

    print(steps)

def is_sequence_repeated(banks, configs):
    for config in configs:
        if banks == config:
            return True
    return False



if __name__ == '__main__':
    main()
