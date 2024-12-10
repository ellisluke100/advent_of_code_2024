import itertools

def evaluate_expression(expression):
    sum = 0
    concat_expr = expression

    # Evaluate operators
    sum = int(concat_expr[0])

    for i in range(0, len(concat_expr)-2, 2):
        op = concat_expr[i+1]
        b = int(concat_expr[i+2])

        match op:
            case '+': sum += b
            case '*': sum *= b
            case '||': sum = int(str(sum) + str(b))

    return sum

problems = []

with open('input.txt', 'r') as file:
    problems = [p.rstrip('\n').split(' ') for p in file.readlines()]

    for p in problems:
        p[0] = p[0].rstrip(':')

operators = ['+', '*', '||']
test_value_sum = 0

for problem in problems:
    test_value = int(problem[0])
    nums = problem[1:]

    operator_locations = len(nums)-1
    operator_permutations = itertools.product(operators, repeat=operator_locations)

    for perm in operator_permutations:
        expression = [x for x in itertools.chain.from_iterable(itertools.zip_longest(nums, perm)) if x]

        # Evaluate expression
        result = evaluate_expression(expression)
        
        if result == test_value:
            test_value_sum += test_value
            break

print("SUM:", test_value_sum)



