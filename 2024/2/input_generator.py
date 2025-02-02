from random import random, randint, choice

# Percentage out of 1
pass_chance = .421 # 421/1000 pass on my real input. This is the probability that it will generate a line that passes part 1.
max_deviation = 5 # Max deviation per number for non-passing levels
lines = 1000
numbers_per_line_range = (5, 8)
initial_number_range = (25, 100)

output = []

for i in range(lines):
    if random() <= pass_chance:
        ascending = choice((-1, 1)) # Choose if it will go up or down
        current_number = randint(initial_number_range[0], initial_number_range[1])
        numbers = [current_number]
        num_count = randint(numbers_per_line_range[0], numbers_per_line_range[1])

        for i in range(num_count):
            change = randint(1, 3) * ascending
            current_number += change
            numbers.append(current_number)

        numbers = map(str, numbers)
        output.append(' '.join(numbers))
    
    else:
        current_number = randint(initial_number_range[0], initial_number_range[1])
        numbers = [current_number]
        num_count = randint(numbers_per_line_range[0], numbers_per_line_range[1])

        for i in range(num_count):
            change = randint(-max_deviation, max_deviation)
            current_number += change
            numbers.append(current_number)

        numbers = map(str, numbers)
        output.append(' '.join(numbers))

file = open("2024/2/input.txt", 'a')
open("2024/2/input.txt", 'w')

for line in output:
    file.write(f"{line}\n")