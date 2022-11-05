
def merge_sort(arr):
    if len(arr)>1:
        left = arr[0:len(arr)//2]
        right = arr[len(arr)//2 : ]
        merge_sort(left )
        merge_sort(right)
        merge_two_sorted_arrays(left,right,arr)


def merge_two_sorted_arrays(a,b,arr):
    i = j = k = 0
    global count
    while i< len(a) and j< len(b):
        if a[i]<=b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
            count+=len(a) - i
        k+=1
    if i< len(a):
        arr[k:] = a[i:]
    else:
        arr[k:] = b[j:]

n = int(input())
arr = list(map(int,input().split()))
count = 0
merge_sort(arr)
print(count)
