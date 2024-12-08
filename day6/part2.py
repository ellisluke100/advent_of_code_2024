import copy

guard = '^'
obstacle = '#'
traversed = 'X'

def find_guard(grid):
    for row in range(0, len(grid)-1):
        for col in range(0, len(grid[row])-1):
            if grid[row][col] == guard:
                return [row, col]

with open('input.txt', 'r') as file:
    lines = [list(l.strip('\n')) for l in file.readlines()]
    row_length = len(lines[0])

out_of_bounds = lambda row,col: row < 0 or row >= len(lines) or col < 0 or col >= len(lines[0])

directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

starting_guard_location = find_guard(lines)

def is_trapped(grid):
    guard_location = starting_guard_location
    curr_start = []
    prev_starts = {0: [], 1: [], 2: [], 3: []}
    direction = 0

    curr_start = guard_location

    while True:
        next_location = [guard_location[0]+directions[direction][0], guard_location[1]+directions[direction][1]]

        if curr_start in prev_starts[direction]:
            return True

        if out_of_bounds(*next_location,):
            # print("OOB: ", *next_location)
            return False

        if grid[next_location[0]][next_location[1]] == obstacle:
            prev_starts[direction].append(curr_start)
            direction = (direction + 1) % len(directions)
            curr_start = guard_location
            continue

        guard_location = next_location

trapped_count = 0

for i in range(0, len(lines)):
    for j in range(0, len(lines)):
        # print(i,j)
        if lines[i][j] not in [obstacle, guard]:
            temp = copy.deepcopy(lines)
            temp[i][j] = obstacle
            if is_trapped(temp): 
                trapped_count += 1
        
print("TRAPPED:", trapped_count)
        

