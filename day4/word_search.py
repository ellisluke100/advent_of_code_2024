# Read data
row_length = None
words = ""
xmas_count = 0

with open("input.txt", "r") as file:
    words = list(line.rstrip('\n') for line in file.readlines())
    row_length = len(words[0])-1

# Horizontals
for line in words:
    xmas_count += line.count('XMAS')
    xmas_count += line.count('SAMX')

# Verticals
for col_i in range(0, row_length):
    # Combine letters in that column into a string
    vertical = []
    for row_i in range(0, len(words)):
        vertical.append(words[row_i][col_i])
    xmas_count += (''.join(vertical)).count('XMAS')
    xmas_count += (''.join(vertical)).count('SAMX')

# Diagonals
diagonals = [(-1, -1), (-1, 1), 
             (1, -1), (1, 1)]

for i in range(0, len(words)):
    for j in range(0, row_length):
        if words[i][j] == "X":
            for diag in diagonals:
                try:
                    if words[i+diag[0]][j+diag[1]] == "M" and words[i+diag[0]*2][j+diag[1]*2] == "A" and words[i+diag[0]*3][j+diag[1]*3] == "S":
                        xmas_count += 1
                except IndexError:
                    continue
            
print("XMAS COUNT:", xmas_count)

# Part 2
cross_xmas_count = 0

for i in range(1, len(words)):
    for j in range(1, row_length):
        if words[i][j] == "A":
            try:
                cross = [
                    ''.join([words[i-1][j-1],words[i][j], words[i+1][j+1]]),
                    ''.join([words[i-1][j+1],words[i][j], words[i+1][j-1]])
                ]
                if (cross[0] == "MAS" or cross[0] == "SAM") and (cross[1] == "MAS" or cross[1] == "SAM"):
                    cross_xmas_count += 1
            except IndexError:
                continue

print("X-MAS COUNT:", cross_xmas_count)
