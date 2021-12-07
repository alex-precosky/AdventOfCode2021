from typing import List

def parse_input(input_str: str) -> List[int]:
    '''Reads the string of the input and make a list of integers out of it'''
    return [int(int_str) for int_str in input_str.strip().split(',')]


def cost_function_part_1(move_distance: int) -> int:
    '''The amount of fuel to move a distance in part 1'''
    return move_distance


def cost_function_part_2(move_distance: int) -> int:
    '''The amount of fuel to move a distance in part 2. Using a recursive function
    with memoization:
    cost(0) = 0
    cost(1) = 1
    cost(n) = cost(n-1) + n
    '''
    global memo

    if move_distance == 0:
        return 0

    if move_distance == 1:
        return 1

    if move_distance in memo:
        return memo[move_distance]

    cost = cost_function_part_2(move_distance - 1) + move_distance
    memo[move_distance] = cost

    return cost


memo = {}
def init_part_2_cost_function():
    '''Initialize the cost function used in part 2'''
    for i in range(1000):
            cost_function_part_2(i)


def calc_min_fuel(distances_list: List[int], cost_function) -> int:
    '''Given a list of crab locations, and cost function, calculate the
    minimum amount of fuel to line them up'''
    min_x = min(distances_list)
    max_x = max(distances_list)

    min_fuel_req = 999999999

    for x in range(min_x, max_x + 1):
        fuel_req = 0

        for distance in distances_list:
            distance_to_move = abs(distance - x)
            fuel_req += cost_function(distance_to_move)

        if fuel_req < min_fuel_req:
            min_fuel_req = fuel_req

    return min_fuel_req


def main():
    input_str = open('input/day07.txt', 'r').read()

    distances_list = parse_input(input_str)

    min_fuel = calc_min_fuel(distances_list, cost_function_part_1)
    print(f'Part 1: Minimum fuel {min_fuel}')

    init_part_2_cost_function()
    min_fuel = calc_min_fuel(distances_list, cost_function_part_2)
    print(f'Part 2: Minimum fuel {min_fuel}')

main()
