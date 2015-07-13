import csv
import sys
import itertools


def count_iter(iterable):
    # count lines in terable
    return sum(1 for _ in iterable)


def setup_iter(reader):
    # Skip first row of the file
    readeriter = iter(reader)
    next(readeriter)

    return readeriter


def list_get(li, pos, default):
    try:
        return li[pos]
    except IndexError:
        return default


if __name__ == '__main__':
    try:
        name_of_file = sys.argv[1]
    except IndexError:
        print 'Usage: python {} filename.csv [start_percent [end_percent]]'.format(sys.argv[0])
        sys.exit(1)

    # maps numbers to frequency those numbers show up
    # so its a histogram
    num_to_freq = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
    }

    start_percent = float(list_get(sys.argv, 2, 0.0))
    end_percent = float(list_get(sys.argv, 3, 1.0))

    with open(name_of_file, 'r') as csvfile:
        reader = csv.reader(csvfile)

        itr1, itr2 = itertools.tee(setup_iter(reader))

        lines = count_iter(itr1)

        start = start_percent * lines
        end = end_percent * lines

        for index, row in enumerate(itr2):
            if index < start:
                continue
            if index >= end:
                break

            for i in row[1].split(','):
                try:
                    toint = int(i)
                except ValueError:
                    continue

                num_to_freq[toint] += 1

    for key, val in num_to_freq.items():
        print "{0}: {1}".format(key, val)
