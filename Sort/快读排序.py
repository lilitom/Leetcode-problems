def quick_sort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists
a=[8,10,9,6,4,16,5,13,26,18,2,45,34,23,1,7,3]
print quick_sort(a,0,len(a)-1)



def parttion(v, left, right):
    key = v[left]
    low = left
    high = right
    while low < high:
        while (low < high) and (v[high] >= key):
            high -= 1
        v[low],v[high] = v[high],v[low]
        while (low < high) and (v[low] <= key):
            low += 1
        v[low], v[high] = v[high], v[low]
    return low
def quicksort(v, left, right):
    if left < right:
        p = parttion(v, left, right)
        quicksort(v, left, p-1)
        quicksort(v, p+1, right)
    return v

s = [6, 8, 1, 4, 3, 9, 5, 4, 11, 2, 2, 15, 6]
print("before sort:",s)
s1 = quicksort(s, left = 0, right = len(s) - 1)
print("after sort:",s1)