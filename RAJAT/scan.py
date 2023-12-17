def scan(head,queue,min,max):
    queue.sort()
    totaldist=0
    if(head-min<max-head):
        totaldist=head-min+max
    else:
        totaldist=max-head+max
    print("Total distance: ",totaldist)
    
queue=[10,22,20,2,40,6,38]
head=20
mincyl=0
maxcyl=100
scan(head,queue,mincyl,maxcyl)