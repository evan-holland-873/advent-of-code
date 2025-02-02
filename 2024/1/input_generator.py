from random import randint

rows = 1000
digits_per_number = 5

output = []
for i in range(rows):
    output.append(f"{randint(10**(digits_per_number-1), 10**digits_per_number)}   {randint(10**(digits_per_number-1), 10**digits_per_number)}")
    
file = open("2024/1/input.txt", 'a')
open("2024/1/input.txt", 'w')

for line in output:
    file.write(f"{line}\n")

file.close()