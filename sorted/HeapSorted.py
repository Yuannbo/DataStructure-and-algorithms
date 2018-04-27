from Sorted.TestHelper import *
# 用数组实现最大堆
# 堆更多用于动态数组的维护


class MaxHeap:

    def __init__(self, capacity):
        # 从下标1开始计数
        self.capacity = capacity
        self.__data = [None]*(capacity+1)
        self.__count = 0

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    def __shift_up(self, k):
        while k > 1 and self.__data[k] > self.__data[k//2]:
            self.__data[k],self.__data[k//2] = \
            self.__data[k//2], self.__data[k]
            k //= 2

        # 递归实现
        # if k > 1:
        #     parent = self.__data[k//2]
        #     if self.__data[k] > parent:
        #         self.__data[k],parent = parent,self.__data[k]
        #         self.__shift_up(k)


    def __shift_down(self,k):
        while 2 * k <= self.__count:
            j = 2 * k   #在此轮循环中data[k]与data[j]交换位置
            if j + 1 <= self.__count and \
                self.__data[j] < self.__data[j+1]:
                j += 1
            if self.__data[k] > self.__data[j]:
                break
            self.__data[k],self.__data[j] = \
            self.__data[j],self.__data[k]
            k = j


    def extract_max(self):
        if self.__count > 0:
            ret = self.__data[1]
            self.__data[1],self.__data[self.__count] = \
            self.__data[self.__count],self.__data[1]
            self.__count -= 1
            self.__shift_down(1)
            return ret

    def get_max(self):
        return self.__data[1]

    def insert(self, item):
        self.__data[self.__count+1] = item
        self.__count += 1
        self.__shift_up(self.__count)

    def heapify(self,arr):
        if self.capacity >= len(arr):
            for i in range(1,len(arr)+1):
                self.__data[i] = arr[i-1]
            self.__count = len(arr)

            for i in range(self.__count//2,0,-1):
                self.__shift_down(i)


    def get_heap(self):
        return self.__data

    def print_heap(self):
        for i in range(1,self.__count+1):
            print(self.__data[i],end=" ")


def heap_sort(l):
    maxheap = MaxHeap(len(l))
    for i in l:
        maxheap.insert(i)
    for i in range(len(l)-1,-1,-1):
        l[i] = maxheap.extract_max()

def heapify_sort(l):
    maxheap = MaxHeap(len(l))
    maxheap.heapify(l)
    for i in range(len(l)-1,-1,-1):
        l[i] = maxheap.extract_max()

def __shift_dowm(l,n,i):
    while 2 * i + 1 < n:
        j = 2 * i + 1 # 在此轮循环中data[k]与data[j]交换位置
        if j + 1 < n and l[j] < l[j + 1]:
            j += 1
        if l[i] > l[j]:
            break
        l[i],l[j] = l[j], l[i]
        i = j

def in_place_heap_sort(l):
    for i in range((len(l)-1)//2,-1,-1):
        __shift_dowm(l,len(l),i)
    for i in range(len(l)-1,0,-1):
        l[i],l[0] = l[0],l[i]
        __shift_dowm(l,i,0)





if __name__ == '__main__':
    l = MaxHeap(100)
    l1 = [1,4,2,2,13,4,5,6,75,32,121,4353,421,432,44]
    # heapify_sort(l1)
    # heap_sort(l1)
    in_place_heap_sort(l1)
    print(is_sorted(l1))
    print(l1)

