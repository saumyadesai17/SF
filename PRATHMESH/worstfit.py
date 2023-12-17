def first_fit(process,memory):
    n=len(process)
    m=len(memory)
    allocation=[-1]*m
    for i in range(n):
        index=-1
        for j in range(m):
            if memory[j]>process[i]:
                index=j
                break
        if index!=-1:
           allocation[i]=index
           memory[index]=memory[index]-process[i]
    for i in range(n):
        print(f'process {i} allocation memory{allocation[i]} with memory {memory[i]}')       
process=[224,350,120,210]        
memory=[250,459,234,123]  
first_fit(process,memory)
           
                