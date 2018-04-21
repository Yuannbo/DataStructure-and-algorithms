def __merge(left, right):
    l, r = 0,0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l = l + 1
        else:
            result.append(right[r])
            r = r + 1
    result += left[l:]
    result += right[r:]
    return result



def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = int(len(list) / 2)
    left = list[:mid]
    right = list[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return __merge(left, right)
