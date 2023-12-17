class PriorityNon():
    def __init__(self,process,at,bt,priority):
        self.process=process
        self.at=at
        self.bt=bt
        self.priority=priority
    def execute(self):
        print('Process Executed in order')
        completion=[]
        pro=[]
        total=0

        for prio,b,p in sorted(zip(self.priority,self.bt,self.process)):
            total=total+b
            pro.append(p)
            completion.append(total)
            print(f'Process {p} with  priority {prio} and {b}')
        #completion.sort(key=pro)
        completion = [x for i, x in sorted(zip(pro, completion))]
        Tat=[c-a for c,a in zip(completion,self.at)]
        wt=[t-b for t,b in zip(Tat,self.bt)]
        print(f'Averag turn over time{sum(Tat)/len(Tat)}')   
        print(f'Average waiting time{sum(wt)/len(wt)}')
            
n=int(input('Enter the number of processes')) 
processes=[]
Burstime=[]  
at=[]
priority=[]
for i in range(0,n):  
    a=input(f'Enter the {i+1} process name')
    c=int(input(f'Enter the {a} process arival time'))
    b=int(input(f'Enter the burst time of {a} process'))  
    d=int(input(f'Enter the priority of {a} process'))  
    processes.append(a)
    Burstime.append(b)   
    at.append(c)
    priority.append(d)
scheduler=PriorityNon(processes,at,Burstime,priority)       
scheduler.execute()         
    
    