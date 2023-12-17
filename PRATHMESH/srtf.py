class SRFT():
    def __init__(self,process,arrival,bt):
        self.process=process
        self.arrival=arrival
        self.bt=bt
    def execute(self):
        remaining={p:t for p,t in zip(self.process,self.bt)}
        completion={p:None for p,t in zip(self.process,self.bt)}
        current_time=0
        while remaining:
            available={p:(t,a) for p,t,a in zip(self.process,self.bt,self.arrival) if t>0 and a<=current_time<=a+t}
            if not available:
                current_time=current_time+1
                continue
            shortest_process=min(available,key=lambda p:available[p][0])
            print(f'Executing {shortest_process} at time {current_time}')    
            remaining[shortest_process]=remaining[shortest_process]-1
            if remaining[shortest_process]==0:
                completion[shortest_process]=current_time
                del remaining[shortest_process]
            current_time=current_time+1 
           
n = int(input('Enter the number of processes: '))
processes = []
burst_time = []
arrival_time = []

for i in range(n):
    a = input(f'Enter the {i+1} process')
    b = int(input(f'Enter the burst time of {i+1} process'))
    c = int(input(f'Enter the arrival time of {i+1} process'))
    processes.append(a)
    burst_time.append(b)
    arrival_time.append(c)

scheduler = SRFT(processes,arrival_time,burst_time)
scheduler.execute()
            
                
                
                    
        
        
           