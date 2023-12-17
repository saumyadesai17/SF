def SSTF(requests,head):
    distance=0
    while requests:
        shortest_request=min( requests,key=lambda x:abs(head-x))
        distance=distance+abs(shortest_request-head)
        print(f'Executing{head}->{shortest_request}')
        head=shortest_request
        requests.remove(shortest_request)
    print(distance)    
request=[40,35,98,44,36]      
head=50
SSTF(request,head)  