def sstf(head,queue):
    totaldist= 0
    while queue:
        nearest_request = min(queue, key=lambda x: abs(x - head))
        totaldist += abs(nearest_request - head)
        head = nearest_request
        queue.remove(nearest_request)
    print("Total distance: ",totaldist)

queue= [98, 183, 37, 122, 14, 124, 65, 67]
head= 53
sstf(head,queue)

