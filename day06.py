# Many fish will have the same timer value... so keep a count of what fish have what timer
# A list of named tuples will hold this info: [[count=3, timer = 10], [count=1, timer=12]}

from collections import namedtuple
from typing import List

TIMER_RESET = 6
TIMER_INIT = 8

FishRecord = namedtuple('FishRecord', ['count', 'timer'])

def parse_fish_str(fish_str: str) -> List[FishRecord]:
    timers = [int(timer_str) for timer_str in fish_str.split(',')]

    fish_list = []

    for timer in timers:
        fish_list = add_or_insert_fish(fish_list, count=1, timer=timer)

    return fish_list


def add_or_insert_fish(fish_list: List[FishRecord], count, timer) -> List[FishRecord]:

    found = False
    output_list = []

    for fish in fish_list:
        if fish.timer == timer:
            output_list.append(FishRecord(count = fish.count + count, timer = timer))
            found = True
        else:
            output_list.append(fish)

    if found is False:
        output_list.append(FishRecord(count = count, timer = timer))

    return output_list


def tick(fish_list: List[FishRecord]) -> List[FishRecord]:
    output_list = []

    for fish in fish_list:
        if fish.timer != 0:
            output_list = add_or_insert_fish(output_list, fish.count, fish.timer - 1)
        else:
            output_list = add_or_insert_fish(output_list, fish.count, TIMER_RESET)
            output_list = add_or_insert_fish(output_list, fish.count, TIMER_INIT)

    return output_list


def count_fish(fish_list: List[FishRecord]) -> int:
    count = 0
    for fish in fish_list:
        count += fish.count

    return count


def play_rounds_and_count_fish(fish_list: List[FishRecord], num_rounds: int) -> int:
    for i in range(num_rounds):
        fish_list = tick(fish_list)

    return count_fish(fish_list)

def main():
    initial_fish_str = open('input/day06.txt', 'r').readlines()[0]
    initial_fish = parse_fish_str(initial_fish_str)

    fish_list = initial_fish.copy()

    ROUNDS = 80
    num_fish = play_rounds_and_count_fish(fish_list.copy(), ROUNDS)
    print(f'After {ROUNDS} rounds, there are {num_fish} fish')

    ROUNDS = 256
    num_fish = play_rounds_and_count_fish(fish_list.copy(), ROUNDS)
    print(f'After {ROUNDS} rounds, there are {num_fish} fish')

main()
