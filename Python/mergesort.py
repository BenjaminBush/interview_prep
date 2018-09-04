def mergesort(alist):
    if len(alist) > 1:
        n = len(alist)
        mid = int(n/2)
        left = alist[:mid]
        right = alist[mid:]

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0

        while k < len(alist) and i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while k < len(alist) and i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1
        
        while k < len(alist) and j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1

        return alist


if __name__ == '__main__':
    alist = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]
    print(mergesort(alist))
