class SJF():
    def __init__(self,processes, burstime):
        self.processes=processes
        self.burstime=burstime
    def execute(self):
        print('Order nof execution')
        for bt,process in sorted(zip(self.burstime,self.processes)):
            print(f'Proces {process} is executing with burstime{bt}')    
n=int(input('Enter the number of processes')) 
processes=[]
Burstime=[]  
for i in range(0,n):  
    a=input(f'Enter the {i+1} process')
    b=int(input(f'Enter the burst time of {i+1} process'))   
    processes.append(a)
    Burstime.append(b)        
scheduler=SJF(processes,Burstime)    
scheduler.execute()    