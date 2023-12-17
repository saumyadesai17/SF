def optimal(pages,capacity):
    hit=0
    page_queue=[]
    for page in pages:
        if page in page_queue:
            hit=hit+1
        elif len(page_queue)<capacity:
            page_queue.append(page)
        else:
            futureindex=[]
            for index,p in enumerate(page_queue):
                if p not in pages[pages.index(page)+1:]:
                    futureindex.append(index)
            if futureindex:
                replace=futureindex[0]
            else:
                replace=0
            page_queue[replace]=page
        print(page_queue)
    print("Hits: ",hit)

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 4
optimal(pages, capacity)
