with open('input', 'r') as f:
    print(
        sum([int(line.strip()) for line in f.readlines()])
    )
