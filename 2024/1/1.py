infile = open("2024/1/input.txt", 'r')
intext = infile.read()
text_lines = intext.splitlines()

left_column = []
right_column = []

for line in text_lines:
    pair = line.split('   ') # 3 spaces
    
    left_column.append(pair[0])
    right_column.append(pair[1])

left_column.sort()
right_column.sort()

sum = 0

for i in range(len(text_lines)): # Easier to do it this way so 'i' can be used as index
    difference = abs(int(left_column[i]) - int(right_column[i]))
    sum += difference

print(f"Part 1: {sum}")

similarity_score = 0

for id in left_column:
    id = int(id)
    multiplier = right_column.count(str(id))
    similarity_score += id * multiplier

print(f"Part 2: {similarity_score}")