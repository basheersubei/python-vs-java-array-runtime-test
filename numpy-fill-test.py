import time
import random
import numpy as np

if __name__ == "__main__":
    
    print("Python run:")
    for arr_size in xrange(10**6, 10**7 + 10**6, 10**6):
        start = time.time()
        arr = np.ndarray(shape=(arr_size,1), dtype=float)
        arr.fill(random.random())
        end = time.time()
        print("time elapsed for " + str(arr_size) + " array size is: " + str(end-start) + " seconds.")
    print("done...")
