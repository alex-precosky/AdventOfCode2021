# Numbers will be drawn from a list one by one into a set() of drawn numbers
# By using a set() it will be easy to use set theory to find unmarked numbers
# on a bingo card and to check for a win

# A bingo card will be represented by a 5x5 numpy array. First dimension is
# y/row, second dimension is x/column

from functools import partial
import numpy as np
from typing import List

BINGO_CARD_DIMENSION = 5  # bingo is played with a 5 by 5 grid of numbers


def parse_drawn_numbers(drawn_numbers_str: str) -> List[int]:
    '''Parses a list of ints out of a comma seperated string of ints'''
    return [int(number_str) for number_str in drawn_numbers_str.split(',')]


def parse_bingo_cards(bingo_cards_strs: List[str]):
    '''Parses bingo cards (i.e. numpy arrays) from a list of strings containing
    many string representations of bingo cards from the input file
    '''
    bingo_card_str = []

    for line in bingo_cards_strs:
        bingo_card_str.extend(line)

    # Produces a list of strings. Each string is a bingo card
    bingo_card_strs = (''.join(bingo_card_str).split('\n\n'))

    # Now parse each bingo card string into a numpy array representation of the
    # bingo card
    bingo_cards = [parse_bingo_card(bingo_card_str) for bingo_card_str in
                   bingo_card_strs]

    return bingo_cards


def parse_bingo_card(bingo_card_str):
    bingo_card = np.zeros([BINGO_CARD_DIMENSION, BINGO_CARD_DIMENSION])

    for row_num, row_str in enumerate(bingo_card_str.split('\n')):
        for col_num, col_str in enumerate(row_str.split()):
            bingo_card[row_num, col_num] = int(col_str)
    return bingo_card


def check_for_win(bingo_card, drawn_numbers: set):
    # Check for vertical wins
    for col_num in range(5):
        col_set = set(bingo_card[:, col_num])
        if col_set.issubset(drawn_numbers):
            return True

    # Check for horizontal wins
    for row_num in range(5):
        row_set = set(bingo_card[row_num, :])
        if row_set.issubset(drawn_numbers):
            return True

    return False


def get_sum_of_unmarked(bingo_card, drawn_set: set):
    card_set = set()

    for row in bingo_card:
        for item in row:
            card_set.add(item)

    unmarked_set = card_set.difference(drawn_set)
    return sum(unmarked_set)


def play_game(bingo_cards, drawn_numbers):
    drawn_so_far = set()

    while True:
        drawn_number = drawn_numbers.pop(0)

        drawn_so_far.add(drawn_number)

        for bingo_card in bingo_cards:
            is_win = check_for_win(bingo_card, drawn_so_far)
            if is_win is True:
                sum_of_unmarked = get_sum_of_unmarked(bingo_card, drawn_so_far)
                print(f'Winner! Score: {sum_of_unmarked * drawn_number}')
                return


def play_game_til_last_win(bingo_cards, drawn_numbers):
    drawn_so_far = set()

    drawn_numbers_copy = drawn_numbers.copy()

    while True:
        drawn_number = drawn_numbers.pop(0)

        drawn_so_far.add(drawn_number)

        bingo_cards = list(filter(lambda card: not check_for_win(card, drawn_so_far), bingo_cards))

        if len(bingo_cards) == 1:
            play_game(bingo_cards, drawn_numbers_copy)
            break


def main():
    input_lines = open('input/day04.txt', 'r').readlines()

    drawn_numbers_str = input_lines[0]
    drawn_numbers = parse_drawn_numbers(drawn_numbers_str)

    bingo_cards = parse_bingo_cards(input_lines[2:])

    play_game(bingo_cards, drawn_numbers.copy())
    play_game_til_last_win(bingo_cards, drawn_numbers.copy())
main()
