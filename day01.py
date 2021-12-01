from typing import List

def count_successive_depth_increases(depths: List[int]):
    successive_depth_increases = 0

    for i in range(len(depths) - 1):
        if depths[i+1] > depths[i]:
            successive_depth_increases += 1

    return successive_depth_increases


def count_successive_3_window_depth_increases(depths: List[int]):
    successive_depth_increases = 0

    for i in range(len(depths) - 3):
        windowA = depths[i] + depths[i+1] + depths[i+2]
        windowB = windowA - depths[i] + depths[i+3]
        if windowB > windowA:
            successive_depth_increases += 1

    return successive_depth_increases


def main():
    infile = 'input/day01.txt'
    depths  = [int(line.strip()) for line in open(infile, 'r').readlines()]

    successive_depth_increases = count_successive_depth_increases(depths)
    print(f'Part 1 - Successive depth increases: {successive_depth_increases}')

    successive_3_window_depth_increases = count_successive_3_window_depth_increases(depths)
    print(f'Part 2 - Successive 3 window depth increases: {successive_3_window_depth_increases}')

main()
