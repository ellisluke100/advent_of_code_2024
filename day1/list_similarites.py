left = []
right = []

# Get input
with open("input.txt", "r") as file:
    lines = file.readlines()
    
    # Each line is like '10345___58492\n', where ___ is spaces
    for line in lines:
        nums = line.split('   ')
      
        left.append(int(nums[0]))
        right.append(int(nums[1].rstrip('\n')))

# Calculate similarity scores
# How often each numebr from the left list (list2) appears in the right list (list1)
nums = dict()
duplicates = dict()

# Go through left; each non-duplicate num becomes a key
# Go through right; increment values for keys if the num is in it
for num in left:
    if not num in nums:
        nums[num] = 0
    else:
        duplicates[num] = 0 
        duplicates[num] += 1

for num in right:
    if nums.get(num) != None or nums.get(num) == 0:
        nums[num] += 1

# Calculate total similary - multiply each num by its similarity score
similarity = 0
for num in nums:
    similarity += num*nums[num]
for duplicate in duplicates:
    similarity += 2*duplicates[duplicate]

print(similarity)

# This is disgusting