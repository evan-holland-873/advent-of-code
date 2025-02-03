### Note: Generated inputs are not accurate, the real inputs have more matches for both days. (140x140)
### They are probably inserted intentionally or selected from many generations.

from random import choice

width = 140
height = 140

characters = ('X', 'M', 'A', 'S')

output = []

for i in range(height):
    for j in range(width):
        output.append(choice(characters))
    output.append('\n')

file = open("2024/4/input.txt", 'w')
file.write(''.join(output))