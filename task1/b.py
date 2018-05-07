#python 3

import threading
import mmap
import time
import contextlib

num_threads = 4

#длина числа в байтах
num_bytes = 4
#количество чисел, считываемых из файла
length = 2**29

mins  = []
maxs = []
sums = []

def reader(thread):
    global mins
    global maxs
    global sums
    
    min_d  = float('INF')
    max_d = -1
    sum_d = 0
    
    with open('file', 'rb') as f:
        #length = os.fstat(f.fileno()).st_size  // num_bytes
        
        #границы окна в байтах, которое читает данный поток
        start_chunk = thread * num_bytes * length // num_threads
        end_chunk = (thread+1) * num_bytes * length // num_threads
        
        with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
            
            for i in range(start_chunk, end_chunk, num_bytes):
                d = int.from_bytes( m[i:i + num_bytes], byteorder='big' )
                
                min_d = min(d, min_d)
                max_d = max(d, max_d)
                sum_d += d
                
    maxs.append(max_d)
    mins.append(min_d)
    sums.append(sum_d)


start_time = time.time()

threads = []
for i in range(num_threads):
    t = threading.Thread(target = reader, args = (i,))
    threads.append(t)
    t.start()
    
for thread in threads:
    thread.join()
    
min_d = min(mins)
max_d = max(maxs)
sum_d = sum(sums)

end_time = time.time()

with open('res', 'a') as f:
    print("min:", min_d, "max:", max_d, "sum:", sum_d, "runtime:", end_time - start_time, file=f)