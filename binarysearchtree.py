data = [2, 4, 6, 12, 45, 75, 89]
target = 89

#Linear Search

def linearSearch(data, target):
    #loop through the list and check if the number is equal to the target
    for i in range(len[data]):
        if data[i] == target:
            return True
        return False

#iterative Binary Search (DIVIDE AND CONQUER)
def binarySearch(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) / 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else: 
            low = mid + 1
    return False