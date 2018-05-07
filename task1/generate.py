#python 3
import random

with open("file", 'wb') as f:
    for i in range(2 ** 29):
        n = random.randint(0, 2 ** 32 - 1)
        f.write(n.to_bytes(4, 'big'))
