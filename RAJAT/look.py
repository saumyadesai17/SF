def look(head,queue,min,max):
    queue.sort()
    m1=queue[0]
    m2=queue[len(queue)-1]
    if(head-min<max-head):
        totaldist=head-m1+m2-m1
    else:
        totaldist=m2-head+m2-m1
    print("Total distance: ",totaldist)
    
queue=[10,22,20,2,40,6,38]
head=20
mincyl=0
maxcyl=100
look(head,queue,mincyl,maxcyl)