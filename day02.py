from typing import List


def follow_basic_commands(commands: List[str]):
    hpos = 0
    depth = 0

    for command in commands:
        parts = command.split(' ')
        direction = parts[0]
        magnitude = int(parts[1])

        if direction == 'forward':
            hpos += magnitude
        elif direction == 'down':
            depth += magnitude
        elif direction == 'up':
            depth -= magnitude

    product = hpos * depth
    print(f'Part 1: Horizontal Position: {hpos} Depth: {depth} Product: {product}')
    return product


def follow_advanced_commands(commands: List[str]):
    hpos = 0
    depth = 0
    aim = 0

    for command in commands:
        parts = command.split(' ')
        direction = parts[0]
        magnitude = int(parts[1])

        if direction == 'forward':
            hpos += magnitude
            depth += aim * magnitude
        elif direction == 'down':
            aim += magnitude
        elif direction == 'up':
            aim -= magnitude

    product = hpos * depth
    print(f'Part 2: Horizontal Position: {hpos} Depth: {depth} Product: {product}')
    return product


def main():
    infile = 'input/day02.txt'
    commands = [line.strip() for line in open(infile, 'r').readlines()]

    follow_basic_commands(commands)
    follow_advanced_commands(commands)

main()
