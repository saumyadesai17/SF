def best_fit(process,memory):
    n=len(process)
    m=len(memory)
    allocation=[0]*m
    for i in range(n):
        best_idx=-1
        for j in range(m):
            if memory[j]>process[i]:
                if best_idx==-1 or memory[j]<memory[best_idx]:
                    best_idx=j
        if best_idx!=-1:
           allocation[i]=best_idx
           memory[best_idx]=memory[best_idx]-process[i]
    for i in range(n):
        print(f'process {i} allocation memory{allocation[i]} with memory {memory[i]}')       
process=[224,350,120,210]        
memory=[250,459,234,123]  
best_fit(process,memory)
           
                