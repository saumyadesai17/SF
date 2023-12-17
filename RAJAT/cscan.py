def cscan(head,queue,min,max):
    queue.sort()
    totaldist=0
    for i in queue:
        if i>head:
            h2=i
            break
    for i in queue[::-1]:
        if i<head:
            h1=i
            break
    if(head-min<max-head):
        totaldist=head-min+max-h2+max-min
    else:
        totaldist=max-head+h1-min+max-min
    print("Total distance: ",totaldist)
    
queue=[10,22,20,2,40,6,38]
head=20
mincyl=0
maxcyl=100
cscan(head,queue,mincyl,maxcyl)