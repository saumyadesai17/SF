from queue import Queue
import threading
import time
buffer=Queue(maxsize=5)
mutex=threading.Semaphore(1)
full=threading.Semaphore(0)
empty=threading.Semaphore(buffer.maxsize)
def producer():
    for i in range(10):
        empty.acquire()
        mutex.acquire()
        print(f'Produced {i}')
        item=i
        buffer.put(item)
        mutex.release()
        full.release()
        time.sleep(1)
def consumer():
    for i in range(10):
        full.acquire()
        mutex.acquire()  
        item=buffer.get() 
        print(f'Consumed {item} item')  
        mutex.release()
        empty.release() 
        time.sleep(1)
produce_thread=threading.Thread(target=producer)   
consumer_thread=threading.Thread(target=consumer)   
produce_thread.start()
consumer_thread.start()
produce_thread.join()
consumer_thread.join()  

    
    