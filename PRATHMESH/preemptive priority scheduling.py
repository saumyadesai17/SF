class Priority():
    def __init__(self,process,priority,bt):
        self.process=process
        self.priority=priority
        self.bt=bt
    def execute (self):   
        execute=[]
        total=0
        remaining=list(self.bt)
        CT={p:None for p in self.process}
        WT={p:None for p in self.process}
        while sum(remaining)!=0:
            print('Infinite')
            available=[(index,b) for index,b in enumerate(remaining) if b>0]
            available.sort(key=lambda x:self.priority[x[0]])
            if not  available:
                break
            process_index,burst_time=available[0]
            execute.append(self.process[process_index])
            if burst_time==1:
                CT[self.process[process_index]]=total+1
                remaining[process_index]=0
            else:
                remaining [process_index]=remaining[process_index]-1
            total=total+1   
        print('Process executing in order','->'.join(execute))        
                
n=int(input('Enter the number of processes')) 
processes=[]
Burstime=[]  
priority=[]
for i in range(0,n):  
    a=input(f'Enter the {i+1} process:')
    b=int(input(f'Enter the burst time of {a} process:'))   
    c=int(input(f'Enter the Priority of {a} process:'))
    processes.append(a)
    Burstime.append(b)   
    priority.append(c) 
scheduler=Priority(processes,priority,Burstime)
scheduler.execute()              
                  
                
        