def fcfs(at, bt):
    n = len(at)
    wt = [0] * n
    tat = [0] * n
    for i in range(1, n):
        wt[i] = (at[i - 1] + bt[i - 1] + wt[i - 1]) - at[i]
        tat[i] = wt[i] + bt[i]
    avgwt = sum(wt) / n
    avgtat = sum(tat) / n
    print("P.No.\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{i + 1}\t\t{at[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")
    print("Average waiting time =", avgwt)
    print("Average turnaround time =", avgtat)

at = [0, 1, 2, 3, 4]
bt = [4, 3, 1, 2, 5]
fcfs(at, bt)
