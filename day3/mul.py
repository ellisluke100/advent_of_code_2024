import re

def mul(a, b):
    return a * b

operations = {
    "mul": mul
}

# Read input
with open("input.txt", "r") as file:
    input_str = file.read()

regex_mul = "mul[(]\\d*,\\d*[)]"
regex_do = "do[(][)]"
regex_dont = "don[']t[(][)]"

big_gex = "|".join([regex_mul, regex_do, regex_dont])

all_statements = re.findall(big_gex, input_str)

sum = 0
enabled = True
disabled = False
for statement in all_statements:
    print(statement)
    if statement == "do()":
        enabled = True
        disabled = False
        continue
    elif statement == "don't()":
        enabled = False
        disabled = True
        continue
    
    if enabled:
        splitted = statement.split(',')
        parameters = {
            "a": int(splitted[0][4:]), 
            "b": int(splitted[1][:-1])
        }
        
        sum += operations["mul"](**parameters)
        continue
    
print(sum)

    
    
