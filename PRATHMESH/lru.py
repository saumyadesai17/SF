def LRU(pages,capacity):
    hit=0
    pages_queue=[]
    for page in pages:
        if page in pages_queue:
            pages_queue.remove(page)
            hit=hit+1
        elif len(pages_queue)==capacity:
            pages_queue.pop(0)
        pages_queue.append(page) 
        print(pages_queue)
    print(hit)
            
pages=[0,3,2,1,4,5,2,1,0,1,7]       
capacity=3
LRU(pages,capacity)    