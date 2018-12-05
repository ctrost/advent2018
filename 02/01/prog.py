import string

with open('../input', 'r') as f:
    ids = [line.strip() for line in f.readlines()]

def contains(n, container_id):
    for char in string.ascii_lowercase:
        if container_id.count(char) == n:
            return 1
    return 0

contains_2 = 0
contains_3 = 0

for container_id in ids:
    contains_2 += contains(2, container_id)
    contains_3 += contains(3, container_id)

print(contains_2 * contains_3)
