import time
import quicksort
import mergesort
import random

# Initialize lists
length = 250000
alist_m = []
for i in range(length):
    alist_m.append(random.randint(0, length))
alist_q = alist_m

start_time_q = time.time()
quicksort.quicksort(alist_q)
end_time_q = time.time()

start_time_m = time.time()
mergesort.mergesort(alist_m)
end_time_m = time.time()

print('Time taken for quicksort : {}'.format(end_time_q - start_time_q))
print('Time taken for mergesort : {}'.format(end_time_m - start_time_m))