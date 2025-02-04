from random import random, randint

# Generated inputs could have an endless loop, make sure to verify

width = 130
height = 130
barrier_chance = .05 # Calculated as 0.050828402 from actual input

output = []
starting_position = (randint(0, height), randint(0, width))

for y in range(height):
    for x in range(width):
        if x == starting_position[1] and y == starting_position[0]:
            output.append('^')
        elif random() <= barrier_chance:
            output.append('#')
        else:
            output.append('.')
    output.append('\n')


file = open("2024/6/input.txt", 'w')
file.write(''.join(output))