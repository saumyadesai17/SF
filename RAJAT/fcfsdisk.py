def fcfs(head,queue):
    totaldist=0
    for i in queue:
        totaldist=totaldist+abs(head-i)
        head=i
    print("Total distance: ",totaldist)
queue=[10,22,20,2,40,6,38]
head=20
fcfs(head,queue)