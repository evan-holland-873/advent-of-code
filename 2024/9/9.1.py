infile = open("2024/9/input.txt")
intext = infile.read()

disk = []

for i, x in enumerate(intext):
    if i % 2 == 0:
        disk.extend((str(i // 2),) * int(x))
    else:
        disk.extend(('.') * int(x))

for i in range(len(disk) - 1, 0, -1):
    if disk[i] != '.':
        leftmost_blank = disk.index('.')

        if i <= leftmost_blank:
            break

        disk[leftmost_blank] = disk[i]
        disk[i] = '.'

checksum = 0

for i, file in enumerate(disk):
    if file == '.':
        break

    checksum += i * int(file)

print(checksum)