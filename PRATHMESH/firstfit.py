def worst_fit(process,memory):
    n=len(process)
    m=len(memory)
    allocation=[0]*m
    for i in range(n):
        worst_idx=-1
        for j in range(m):
            if memory[j]>process[i]:
                if worst_idx==-1 or memory[j]>memory[worst_idx]:
                    worst_idx=j
        if worst_idx!=-1:
           allocation[i]=worst_idx
           memory[worst_idx]=memory[worst_idx]-process[i]
    for i in range(n):
        print(f'process {i} allocation memory{allocation[i]} with memory {memory[i]}')       
process=[224,350,120,210]        
memory=[250,459,234,123]  
worst_fit(process,memory)
           
                