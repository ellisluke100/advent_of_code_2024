### Part 1
# Rules
rules = {}

with open("rules.txt", "r") as rules_file:
    lines = [r.rstrip('\n') for r in rules_file.readlines()]
    
    for line in lines:
        nums = line.split('|')

        if not rules.get(nums[0]):
            rules[nums[0]] = [nums[1]]
        else:
            rules[nums[0]].append(nums[1])

# Updates
correct_mid_total = 0
bad_updates = []

updates = []
def is_correct(update):
    for i in range(1, len(update)):
        rule = rules.get(update[i])

        if rule:
            pre_nums = update[:i]
            
            if [num for num in pre_nums if num in rule]:
                return False
        
    return True

with open("input.txt", "r") as updates_file:
    lines = [u.rstrip('\n').split(',') for u in updates_file.readlines()]

    for update in lines:
        updates.append(updates)

        if is_correct(update):
            correct_mid_total += int(update[len(update)//2])
        else:
            bad_updates.append(update)

# Output
print("Correct mid total:", correct_mid_total)

### Part 2
new_mid_total = 0

# Credit to https://github.com/hansenwebco/advent-of-code-2024/blob/master/code-day05-02-code.py for the approach
for update in bad_updates:
    i = 0
    while i < len(update)-1:
        curr = update[i]
        next = update[i+1]

        if curr in rules[next]:
            # Swappity swap
            update[i] = next
            update[i+1] = curr
            i = 0
        else:
            i += 1

    new_mid_total += int(update[len(update)//2])

print("New mid total:", new_mid_total)



        
