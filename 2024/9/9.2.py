infile = open("2024/9/input.txt")
intext = infile.read()

disk = []

for i, x in enumerate(intext):
    if i % 2 == 0:
        disk.extend((chr((i // 2)+97),) * int(x)) # Need to add 97 (potentially less) because the control characters mess with it I think
    else:
        disk.extend(('.') * int(x))

current_id_counter = 0

#print(''.join(disk))

for i in range(len(disk) - 1, 0, -1):
    print(i)
    if disk[i] == '.': continue

    current_id_counter += 1

    if disk[i - 1] != disk[i]:

        current_id = disk[i]

        try:
            first_available_blank = ''.join(disk).index(('.' * current_id_counter))
        except ValueError:
            current_id_counter = 0
            continue

        if first_available_blank > i:
            current_id_counter = 0
            continue

        for j in range(current_id_counter):
            disk[first_available_blank + j], disk[i + j] = current_id, '.'
        
        #print(''.join(disk))

        current_id_counter = 0


checksum = 0

for i, file in enumerate(disk):
    if file == '.':
        continue

    checksum += i * (ord(file)-97)

print(checksum)