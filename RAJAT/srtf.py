def srtf(at, bt):
    n = len(at)
    wt = [0] * n
    tat = [0] * n
    for i in range(n):
        if i > 0 :
            wt[i] = max(0, tat[i - 1] - at[i]) 
        else:
            wt[i]=0  
        tat[i] = bt[i] + wt[i]
    total_wt = sum(wt)
    total_tat = sum(tat)
    print("Processes\tArrival Time\tBurst Time\tWaiting Time\tTurn-Around Time")
    for i in range(n):
        print(f"   {i + 1}\t\t{at[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")
    print("\nAverage waiting time = {:.5f}".format(total_wt / n))
    print("Average turn around time = {:.5f}".format(total_tat / n))

at = [1, 1, 2, 3]
bt = [6, 8, 7, 3]
srtf(at, bt)
