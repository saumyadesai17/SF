def sjf(at, bt):
    n = len(at)
    ct = [0] * n
    wt = [0] * n
    tat = [0] * n
    for i in range(n):
        ct[i] = (max(ct[i-1], at[i])+bt[i])
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]

    print("Process\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{i+1}\t\t{at[i]}\t\t{bt[i]}\t\t{ct[i]}\t\t{wt[i]}\t\t{tat[i]}")
    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n
    print(f"\nAverage Waiting Time: {avg_wt}")
    print(f"Average Turnaround Time: {avg_tat}")
    
at = [0, 2, 4, 5]
bt = [7, 4, 1, 4]
sjf(at, bt)

