import random
import time
#生成有n个元素的随机数组，范围为[rangeL,rangeR]
def generate_random_array(n,rangeL, rangeR):
    l = [None]*n
    for i in range(n):
        l[i] = random.randint(rangeL,rangeR)
    return l

# 用于对比列表的插入与赋值的效率
def generate_random_array2(n,rangeL, rangeR):
    l = []
    for i in range(n):
        l.append(random.randint(rangeL,rangeR))
    return l

# 判断数组是否有序
def is_sorted(l):
    for i in range(1,len(l)):
        if l[i-1] > l[i]:
            return False
    return True

# 测试算法的时间
def test_sort(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    # 将正确性测试放入具体排序函数中
    # if is_sorted(l):
    print(func.__name__ + " : " + str(end_time-start_time) + "s")

if __name__ == '__main__':
    test_sort(generate_random_array,1000000,1,10000)
    test_sort(generate_random_array2,1000000,1,10000)

