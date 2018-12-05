with open('input', 'r') as f:
    changes = [int(line.strip()) for line in f.readlines()]

frequencies = [0]
frequency = 0
found = False

while not found:
    for change in changes:
        frequency += change
        if frequency in frequencies:
            found = True
            break
        frequencies.append(frequency)
        
print(frequency)
