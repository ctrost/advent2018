with open('../input', 'r') as f:
    ids = [line.strip() for line in f.readlines()]

def diff(id1, id2):
    for i in range(len(id1)):
        if id1[i] != id2[i]:
            id1 = id1[:i] + id1[i+1:]
            id2 = id2[:i] + id2[i+1:]
            if id1 == id2: 
                return id1
            else:
                return False
    
for i, container_id in enumerate(ids):
    for other_container_id in ids[i:]:
        if diff(container_id, other_container_id):
            print(diff(container_id, other_container_id))
            break


