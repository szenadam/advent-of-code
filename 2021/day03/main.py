import numpy as np


def main():

    #input = open('sample_input.txt', 'r')
    input = open('input.txt', 'r')

    data = []

    for line in input.readlines():
        data.append(line.strip())

    print(f"DATA: {input.name}")
    print('-' * 20)
    part_one(data)
    print('-' * 20)
    part_two(data)
    print('-' * 20)

    return 0


def part_two(data):
    splitted_data = []

    for d in data:
        s = [char for char in d]
        splitted_data.append(s)

    matrix = np.array(splitted_data)
    oxygen_generator_rating = get_oxygen_generator_rating(matrix)
    co2_scrubber_rating = get_co2_scrubber_rating(matrix)
    print(f"OXYGEN GENERATOR RATING: {oxygen_generator_rating}")
    print(f"OXYGEN CO2 SCRUBBER RATING: {co2_scrubber_rating}")
    print(f"LIFE SUPPORT RATING: {oxygen_generator_rating * co2_scrubber_rating}")


def get_oxygen_generator_rating(matrix):
    temp_data = matrix
    data_length = len(matrix[0])
    for i in range(data_length):
        if len(temp_data) == 1:
            break
        most_common_bit = most_common_value(temp_data.T[i], '1')
        temp_data = filter_by_value_at_position(temp_data, most_common_bit, i)
    return int('0b' + ''.join(temp_data[0]), 2)


def get_co2_scrubber_rating(matrix):
    temp_data = matrix
    data_length = len(matrix[0])
    for i in range(data_length):
        if len(temp_data) == 1:
            break
        least_common = least_common_value(temp_data.T[i], '0')
        temp_data = filter_by_value_at_position(temp_data, least_common, i)
    return int('0b' + ''.join(temp_data[0]), 2)


def filter_by_value_at_position(data, val, pos):
    result = []
    for d in data:
        if d[pos] == val:
            result.append(d)
    return np.array(result)


def most_common_value(v, fallback_value):
    ones_count = np.count_nonzero(v == '1')
    zeros_count = np.count_nonzero(v == '0')
    if ones_count > zeros_count:
        return '1'
    elif ones_count < zeros_count:
        return '0'
    else:
        return fallback_value


def least_common_value(v, fallback_value):
    ones_count = np.count_nonzero(v == '1')
    zeros_count = np.count_nonzero(v == '0')
    if ones_count > zeros_count:
        return '0'
    elif ones_count < zeros_count:
        return '1'
    else:
        return fallback_value


def part_one(data):
    splitted_data = []

    for d in data:
        s = [char for char in d]
        splitted_data.append(s)

    matrix = np.array(splitted_data)
    transposed = matrix.T

    gamma_rate = []
    epsilon_rate = []

    for t in transposed:
        number_of_zeros = 0
        number_of_ones = 0
        for i in t:
            if i == '0':
                number_of_zeros += 1
            else:
                number_of_ones += 1

        if number_of_zeros > number_of_ones:
            gamma_rate.append('0')
            epsilon_rate.append('1')
        else:
            gamma_rate.append('1')
            epsilon_rate.append('0')

    binary_gamma_rate = bin(int('0b' + ''.join(gamma_rate), 2))
    binary_epsilon_rate = bin(int('0b' + ''.join(epsilon_rate), 2))
    decimal_gamma_rate = int(binary_gamma_rate, 2)
    decimal_epsilon_rate = int(binary_epsilon_rate, 2)

    print(f"GAMMA RATE: {decimal_gamma_rate}")
    print(f"EPSILON RATE: {decimal_epsilon_rate}")
    print(f"POWER CONSUMPTION: {decimal_gamma_rate * decimal_epsilon_rate}")


if __name__ == "__main__":
    main()
