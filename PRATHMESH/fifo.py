def FIFO(requests,head):
    distance=0
    while requests:
        shortest_request=requests[0]
        distance=distance+abs(shortest_request-head)
        print(f'Executing{head}->{shortest_request}')
        head=shortest_request
        requests.remove(shortest_request)
    print(distance)    
request=[40,35,98,35,36]      
head=50
FIFO(request,head)  