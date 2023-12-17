def clook(head,queue,min,max):
    queue.sort()
    m1=queue[0]
    m2=queue[len(queue)-1]
    for i in queue:
        if i>head:
            h2=i
            break
    for i in queue[::-1]:
        if i<head:
            h1=i
            break
    totaldist=0
    if(head-min<max-head):
        totaldist=head-m1+m2-h2+m2-m1
    else:
        totaldist=m2-head+h1-m1+m2-m1
    print("Total distance: ",totaldist)
    
queue=[82,170,43,140,24,16,190]
head=50
mincyl=0
maxcyl=200
clook(head,queue,mincyl,maxcyl)