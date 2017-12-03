def get_list_of_digits(file):
    seq = []

    with open(file) as f:
        for line in f:
            for dig in line:
                if dig.isdigit():
                    seq.append(int(dig))

    return seq

def sum_next_digits(seq):
    sum_of_digits = 0

    for i in range(len(seq)-1):
        if seq[i] == seq[i+1]:
            sum_of_digits += seq[i]

    if seq[len(seq)-1] == seq[0]:
        sum_of_digits += seq[len(seq)-1]

    return sum_of_digits

def sum_halfway_around_digits(seq):
    sum_of_digits = 0
    halfway = int(len(seq)/2)

    for i in range(halfway):
        if seq[i] == seq[halfway + i]:
            sum_of_digits += seq[i]*2

    return sum_of_digits

def main():
    seq = get_list_of_digits("sequence.csv")
    sum_next = sum_next_digits(seq)
    sum_halfway = sum_halfway_around_digits(seq)
    print(sum_next, sum_halfway)
    

if __name__ == '__main__':
    main()
