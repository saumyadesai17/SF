def CScan(requests,head,start,end,direction):
    distance=0
    if direction=='left':
        requests.append(start)
        requests.append(end)
        requests.sort()
        left_sequence=[i for i in requests if head>i]
        right_sequence=[i for i in requests if head<i]
        left_sequence.sort(reverse=True)
        right_sequnce.sort(reverse=True)
        while left_sequence:
            request=left_sequence[0]
            distance=distance+abs(head-request)
            print(f'{head}->{request}')
            head=request
            left_sequence.remove(request)
        while right_sequence:
            request=right_sequence[0]
            distance=distance+abs(head-request)
            print(f'{head}->{request}')
            head=request
            right_sequence.remove(request)
    if direction=='right':
        requests.append(end)
        requests.append(start)
        requests.sort()
        left_sequence=[i for i in requests if head>i]
        right_sequence=[i for i in requests if head<i]
        left_sequence.sort()
        right_sequence.sort()
        while right_sequence:
            request=right_sequence[0]
            distance=distance+abs(head-request)
            print(f'{head}->{request}')
            head=request
            right_sequence.remove(request)
        while left_sequence:
            request=left_sequence[0]
            distance=distance+abs(head-request)
            print(f'{head}->{request}')
            head=request
            left_sequence.remove(request)    
    return distance        

requests=[176,79,34,60,92,11,41,114]
start=0
end=199
head=50
print(CScan(requests,head,start,end,'right'))
                  