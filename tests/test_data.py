"""
test_data.py

Reads, cleans and returns a list of solved or unsolved sudoku puzzle strings
contained in the file provided

:created on: 20160616
__author__ = 'Frederic Dupont'
:License: GPL3
"""


def read_data_from(filename):
    """
    reads the text in file_name
    :rtype: list
    :param filename: The name of the file to read
    :return: the list of the file content
    """
    with open(filename, 'r') as file:
        data = file.readlines()
    return data


def filter_and_clean(raw_data):
    """
    strips white space, tabs and line feeds at end of each line
    omits lines starting with '#'
    :param raw_data:
    :return: a python list of cleaned up data
    """
    clean_data = []
    for line in raw_data:
        line = line.strip(' \t\n\r')
        if line.startswith('#') or len(line) == 0:
            continue
        elif all(char.isdigit() or (char == '.') for char in line):
            clean_data.append(line)
    return clean_data


def get_data_from(filename):
    """
    obtains cleaned up data from filename
    :param filename: name of the file we want to obtain data from
    :return: a python list of cleaned up data [list of strings of digits or '.'
    """
    raw_data = read_data_from(filename)
    clean_data = filter_and_clean(raw_data)
    return clean_data


if __name__ == '__main__':
    filenames = ['solved_10000_grids_startwith_123456789.txt',
                 'unsolved_10000_grids_45_numbers.txt',
                 'unsolved_10000_grids_40_numbers.txt',
                 'unsolved_10000_grids_35_numbers.txt',
                 'unsolved_10000_grids_30_numbers.txt',
                 'unsolved_10000_grids_25_numbers.txt']

    for filename in filenames:
        raw_data = get_data_from('../resources/' + filename)
        clean_data = filter_and_clean(raw_data)
        print(filename)
        for line in clean_data[:10]:
            print(line)
        print()

