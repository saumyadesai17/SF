def round_robin(process,Burst_time,quantum):
    n=len(process)
    remaining=Burst_time.copy()
    tat=[0]*n
    wt=[0]*n
    total=0
    rem=n
    execution=[]
    while rem>0:
        for i in range(n):
            #print('helli')
            if remaining[i]>0:
                run_time=min(quantum,remaining[i])
                total=total+run_time
                remaining[i]=remaining[i]-run_time
                
                for k in range(run_time):
                    execution.append(str(i))
                    
                wt[i]=max(0,total-Burst_time[i])
                if remaining[i]==0:
                    rem=rem-1
            tat[i]=wt[i]+Burst_time[i]
    print('Execution order is','->'.join(execution))    
    print(sum(tat)/n)
    print(sum(wt)/n)
process=[1,2,3]
bt=[10,5,8]
quantum=3
round_robin(process,bt,quantum)
               
                
                
    