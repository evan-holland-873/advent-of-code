from random import randint

mode = 'disksize'
input_size = 25
disk_size = 149

output = []

match (mode):
    case 'inputsize':
        for i in range(input_size):
            output.append(str(randint(1, 9)))
    case 'disksize':
        while sum(output) < disk_size - 9:
            output.append(randint(1,9))
        output.append(disk_size - sum(output))
        output = map(str, output)
    
file = open("2024/9/input.txt", 'w')
file.write(''.join(output))
file.close()