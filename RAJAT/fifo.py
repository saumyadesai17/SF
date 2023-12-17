def fifo(pages,capacity):
    page_queue=[]
    hit=0
    for page in pages:
        if page not in page_queue:
            if len(page_queue)==capacity:
                page_queue.pop(0)
            page_queue.append(page)
        else:
            hit=hit+1
        print(page_queue)
    print("Hits: ",hit)

p=[7,0,1,2,0,3,0,4,2,3,0,3,2]
c=4
fifo(p,c)