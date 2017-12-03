def get_list_of_digits(file):
    seq = []
    with open(file) as f:
        for line in f:
            for dig in line:
                if dig.isdigit():
                    seq.append(int(dig))

    return seq

def sum_next_digits(seq):

    sum = 0

    for i in range(len(seq)-1):
        if seq[i] == seq[i+1]:
            sum += seq[i]

    if seq[len(seq)-1] == seq[0]:
        sum += seq[len(seq)-1]

    return sum

def main():

    seq = get_list_of_digits("sequence.csv")
    sum_next = sum_next_digits(seq)
    print(sum_next)


if __name__ == '__main__':
    main()
