# If hitting a obstacle, just turn the grid 90 degrees
# Looking for guard_location + 1 - if out of bounds, end the search
# Upon moving, set the guard location to a special character
# Count these at the end

obstacle_char = '#'
traversed_char = 'X'
guard_char = '^'
directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]
dir_i = 0

guard_location = []

# Guard hits an obstacle: 90 degree turn
# Else, move up

with open('input.txt', 'r') as file:
    lines = [list(l.strip('\n')) for l in file.readlines()]
    row_length = len(lines[0])

def find_guard(grid):
    for row in range(0, len(grid)-1):
        for col in range(0, len(grid[row])-1):
            if grid[row][col] == guard_char:
                return [row, col]

# Where the guard at? (initially)
guard_location = find_guard(lines)

# Move that guard
# rotate = lambda l: list(zip(*l[::-1]))
moving = True

guard_locations = []

while moving:
    direction = directions[dir_i]
    new_guard_location = [guard_location[0] + direction[0], guard_location[1] + direction[1]]
    
    try:
        next_in_path = lines[new_guard_location[0]][new_guard_location[1]]

        if next_in_path == obstacle_char:
            # Turn that guard
            dir_i = (dir_i + 1) % len(directions)
        else:
            # Move that guard
            lines[guard_location[0]][guard_location[1]] = traversed_char
            guard_locations.append(guard_location)
            guard_location = new_guard_location
        
    except IndexError:
        lines[guard_location[0]][guard_location[1]] = traversed_char
        moving = False
    
count = 0
for row in range(0, len(lines)):
    for col in range(0, len(lines[row])):
        if lines[row][col] == traversed_char:
            count += 1

print(count)