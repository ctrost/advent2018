from sys import exit

with open('../input', 'r') as f: 
    ids = [line.strip() for line in f.readlines()]

def diff1(id1, id2):
    for i, chars in enumerate(zip(id1, id2)):
        if chars[0] != chars[1]:
            if (id1[:i] + id1[i+1:]) == (id2[:i] + id2[i+1:]):
                return id1
            else:
                return False
    
for i, container_id in enumerate(ids):
    for other_container_id in ids[i:]:
        found_it = diff1(container_id, other_container_id)
        if found_it:
            print(found_it)
            exit(0)


