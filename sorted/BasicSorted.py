from Sorted.TestHelper import *

def selet_sort(l):
    for i in range(len(l)):
        minindex = i
        for j in range(i+1,len(l)):
            if l[j] > l[minindex]:
                j = minindex
            l[j],l[minindex] = l[minindex],l[j]
    return l


if __name__ == '__main__':
    l = generate_random_array(1000, 1,100)
    test_sort(selet_sort, l)

