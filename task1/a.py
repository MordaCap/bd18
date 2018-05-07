#python 3

import time
import os

num_bytes = 4
length = 2 ** 29

min_d  = float('INF')
max_d = -1
sum_d = 0

start_time = time.time()

with open('file', 'rb') as f:
    #length = os.fstat(f.fileno()).st_size  // num_bytes
    
    for i in range(length):
        d = int.from_bytes(f.read(num_bytes), byteorder='big')
        
        min_d = min(d, min_d)
        max_d = max(d, max_d)
        sum_d += d

end_time = time.time()

with open('res', 'a') as f:
    print("min:", min_d, "max:", max_d, "sum:", sum_d, "runtime:", end_time - start_time, file=f)