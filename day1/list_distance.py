left = []
right = []

cumulative_diff = 0

# Get input
with open("input.txt", "r") as file:
    lines = file.readlines()
    
    # Each line is like '10345___58492\n', where ___ is spaces
    for line in lines:
        nums = line.split('   ')
      
        left.append(int(nums[0]))
        right.append(int(nums[1].rstrip('\n')))

# Calculate distance
# Lists must be sorted (smallest first)
# Get difference between each pair of numbers, and collate
left.sort()
right.sort()

count = 0

for i in range(0, len(left)):
    diff = abs(left[i] - right[i])
    cumulative_diff += diff

print(cumulative_diff)