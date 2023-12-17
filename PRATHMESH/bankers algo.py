def banker(alloc,max,avail):
    n=len(alloc)
    m=len(avail)
    finish=[False]*n
    safe_sequence=[]
    need=[[max[i][j]-alloc[i][j] for j in range(m)]for i in range(n)]
    for k in range(n):
        for i in range(n):
            if not finish[i] and all([need[i][j]<=avail[j] for j in range(m)]):
                avail=[avail[j]+alloc[i][j] for j in range(m)]
                finish[i]=True
                safe_sequence.append(i)
    return safe_sequence if all(finish) else None
               
            
alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
max = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
avail = [3, 3, 2]

result = banker(alloc, max, avail)
print("Safe Sequence:", result) if result is not None else print("The system is in an unsafe state.")            