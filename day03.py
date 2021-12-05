from typing import List


def calc_gamma_rate(binary_input: List[str]) -> List[int]:
    '''Given the list of binary strings, find the gamma rate, which
    is a new binary string where each bit is the value of the most common
    bit in each position of the binary strings in binary_input
    '''
    strlen = len(binary_input[0])

    one_counts = [0] * strlen

    one_counts, zero_counts = calc_one_and_zero_counts(binary_input)

    gamma_rate = [0] * strlen
    for i, one_count in enumerate(one_counts):
        if one_count > len(binary_input) / 2:
            gamma_rate[i] = 1

    return gamma_rate


def calc_one_and_zero_counts(binary_input: List[str]):
    '''Count how many ones and how many zeros are in each bit position in the
    binary strings of binary_input
    '''
    strlen = len(binary_input[0])

    one_counts = [0] * strlen
    zero_counts = [0] * strlen

    for bit in range(strlen):
        for item in binary_input:
            if item[bit] == '1':
                one_counts[bit] += 1
            else:
                zero_counts[bit] += 1

    return one_counts, zero_counts


def calc_oxygen_generator_rating(binary_input: List[str]):

    strlen = len(binary_input[0])

    remaining_input = binary_input.copy()
    for bit in range(strlen):
        one_counts, zero_counts = calc_one_and_zero_counts(remaining_input)
        next_remaining_input = []

        if one_counts[bit] >= zero_counts[bit]:  # we keep 1's in the case of a tie
            most_common_bit = 1
        else:
            most_common_bit = 0

        for item in remaining_input:
            if int(item[bit]) == most_common_bit:
                next_remaining_input.append(item)

        if len(remaining_input) == 1:
            break

        remaining_input = next_remaining_input.copy()

    return_list = [int(ch) for ch in remaining_input[0]]

    return bit_list_to_int(return_list)


def calc_co2_scrubber_rating(binary_input: List[str]):

    strlen = len(binary_input[0])

    remaining_input = binary_input.copy()
    for bit in range(strlen):
        one_counts, zero_counts = calc_one_and_zero_counts(remaining_input)
        next_remaining_input = []

        if one_counts[bit] >= zero_counts[bit]: # we keep 0's in the case of a tie
            least_common_bit = 0
        else:
            least_common_bit = 1

        for item in remaining_input:
            if int(item[bit]) == least_common_bit:
                next_remaining_input.append(item)

        if len(remaining_input) == 1:
            break

        remaining_input = next_remaining_input.copy()

    return_list = [int(ch) for ch in remaining_input[0]]

    return bit_list_to_int(return_list)


def bit_list_to_int(bit_list: List[int]) -> int:
    '''Convert a list of binary digits to an int'''
    bitlen = len(bit_list)

    sum = 0
    for i, bit in enumerate(bit_list):
        exp = bitlen - i - 1
        if bit == 1:
            sum += pow(2, exp)

    return sum


def invert_bit_list(bit_list: List[int]) -> List[int]:

    return_list = [0] * len(bit_list)

    for i, bit in enumerate(bit_list):
        if bit_list[i] == 0:
            return_list[i] = 1

    return return_list


def main():
    infile = 'input/day03.txt'
    lines = [line.strip() for line in open(infile, 'r').readlines()]

    gamma_rate = calc_gamma_rate(lines)
    gamma = bit_list_to_int(gamma_rate)

    epsilon_bits = invert_bit_list(gamma_rate)
    epsilon = bit_list_to_int(epsilon_bits)

    print(f'Part 1: Power consumption is: {gamma * epsilon}')

    oxygen_generator_rating = calc_oxygen_generator_rating(lines)
    co2_scrubber_rating = calc_co2_scrubber_rating(lines)

    print(f'Part 2: Life support rating is: {oxygen_generator_rating * co2_scrubber_rating}')

main()
