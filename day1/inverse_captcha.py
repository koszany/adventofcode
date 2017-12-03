def sum_of_matching_digits(file):

    seq = []
    with open(file) as f:
        for line in f:
            for dig in line:
                if dig.isdigit():
                    seq.append(int(dig))

    sum = 0

    for i in range(len(seq)-1):
        if seq[i] == seq[i+1]:
            sum += seq[i]

    if seq[len(seq)-1] == seq[0]:
        sum += seq[len(seq)-1]

    return sum

def main():

    sum = sum_of_matching_digits("sequence.csv")
    print(sum)

if __name__ == '__main__':
    main()
