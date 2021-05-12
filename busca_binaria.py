num = input().split()

array = [int(num[i]) for i in range(1, int(num[0])+1)]
array_id = [int(num[i]) for i in range(int(num[0])+1, len(num))]


def binary_search(array, target, start=0, end=None, count=0):
    if end is None:
        end = len(array) - 1

    if start <= end:
        mid = (start + end)//2

        if target == array[mid]:
            count+=1
            return count

        elif target > array[mid]:
            count +=1
            return binary_search(array, target, mid+1, end, count)
    
        elif target < array[mid]:
            count +=1
            return binary_search(array, target, start, mid-1, count)
    else:
        return count
    

for i in array_id: 
    print(binary_search(array, i), end=' ')
