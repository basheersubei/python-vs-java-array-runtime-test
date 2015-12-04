import time
import random

if __name__ == "__main__":
    
    print("Python run:")
    for arr_size in xrange(10**6, 10**7 + 10**6, 10**6):
        start = time.time()
        arr = [0] * arr_size
        ran = random.random()
        for i in xrange(1, arr_size):
            arr[i] = ran
        end = time.time()
        print("time elapsed for " + str(arr_size) + " array size is: " + str(end-start) + " seconds.")
    print("done...")
