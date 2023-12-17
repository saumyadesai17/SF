def lru(pages,capacity):
    page_queue=[]
    hit=0
    for page in pages:
        if page in page_queue:
            hit=hit+1
            page_queue.remove(page)
        elif len(page_queue)==capacity:
            page_queue.pop(0)
        page_queue.append(page)
        print(page_queue)
    print("Hits: ",hit)

pages = [7,0,1,2,0,3,0,4,2,3,0,3,2]
capacity = 4
lru(pages,capacity)


