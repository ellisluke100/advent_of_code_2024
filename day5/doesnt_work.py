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

# Luke mode
counto = 0
with open("input.txt", "r") as updates_file:
    lines = [u.rstrip('\n').split(',') for u in updates_file.readlines()]

    is_good = lambda update: not all(set(update[:i]) & set(rules[update[i]]) for i in range(1, len(update)))
    counter = sum(int(update[len(update)//2]) for update in lines if is_good(update))

    print(counter)