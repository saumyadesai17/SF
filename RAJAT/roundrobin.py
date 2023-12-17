def round_robin(processes, bt, quantum):
    n = len(processes)
    wt = [0]*n 
    tat = [0]*n
    rem_bt=bt.copy()
    t=0
    rem = n
    while rem > 0:
        for i in range(n):
            if rem_bt[i] > 0:
                run_time = min(quantum, rem_bt[i])
                t += run_time
                rem_bt[i] -= run_time
                wt[i] = max(0, t - bt[i])
                if rem_bt[i] == 0:
                    rem -= 1
            tat[i] = bt[i] + wt[i]
    print("Processes Burst Time\t Waiting Time Turn-Around Time")
    for i in range(n):
        print(" ", processes[i], "\t\t", bt[i], "\t\t", wt[i], "\t\t", tat[i])
    avg_wt = sum(wt)/n 
    avg_tat = sum(tat)/n
    print("\nAverage waiting time = {:.5f}".format(avg_wt))
    print("Average turn around time = {:.5f}".format(avg_tat))

p = [1, 2, 3]
tq = 3
bt = [10, 5, 8]
round_robin(p, bt, tq)
