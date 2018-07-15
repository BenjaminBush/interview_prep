def quicksort(alist):
    return quicksort_helper(alist, 0, len(alist) - 1)

def quicksort_helper(alist, lo, hi):
    if lo < hi:
        pivot = partition(alist, lo, hi)
        quicksort_helper(alist, lo, pivot-1)
        quicksort_helper(alist, pivot+1, hi)


def partition(alist, lo, hi):
    '''
    Satisfies 3 invariants
    1) alist[j] is in its final place in array for some j
    2) no entry in alist[:j] is greater than alist[j]
    3) no entry in alist[j:] is less than alist[j]
    '''
    pivot_val = alist[lo]                                                   # Element selected to be in final position

    left_p = lo + 1
    right_p = hi

    done = False
    while not done:
        while left_p <= right_p and alist[left_p] <= pivot_val:
            left_p += 1
        while right_p >= left_p and alist[right_p] >= pivot_val:
            right_p -= 1
        if left_p > right_p:                                                # Invariants 2,3 satisfied
            done = True
        else:                                                               # Swap the elements at left_p and right_p to achieve invariants 2, 3
            temp = alist[left_p]
            alist[left_p] = alist[right_p]
            alist[right_p] = temp

    # Satisfy invariant 1
    temp = alist[lo]
    alist[lo] = alist[right_p]
    alist[right_p] = temp

    return right_p


if __name__ == '__main__':
    alist = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]
    quicksort(alist)
    print(alist)