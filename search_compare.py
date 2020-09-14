import time
import random
import statistics


def list_generator():
    list500 = [random.choices(range(1, 101), k=500) for num in range(100)]
    list1000 = [random.choices(range(1, 101), k=1000) for num in range(100)]
    list10000 = [random.choices(range(1, 101), k=10000) for num in range(100)]
    return list500, list1000, list10000


def sort_list(ulg):
    slg = []
    for i in ulg:
        i.sort()
        slg.append(i)
    return slg[0], slg[1], slg[2]


def sequential_search(a_list, item):
    time_avg, time_total_avg = [], []
    pos = 0
    found = False
    for i in a_list:
        for ii in i:
            time_start = time.time()
            while pos < len(ii) and not found:
                if ii[pos] == item:
                    found = True
                else:
                    pos = pos + 1
            time_end = time.time()
            # print(time_end,time_start)
            time_avg.append(float(time_end - time_start))
        # print(len(time_avg))
        time_total_avg.append(statistics.mean(time_avg))
        time_avg = []
    time_total_avg = statistics.mean(time_total_avg)
    return found, time_total_avg


def ordered_sequential_search(a_list, item):
    time_avg, time_total_avg = [], []
    pos = 0
    found = False
    stop = False
    for i in a_list:
        for ii in i:
            time_start = time.time()
            while pos < len(ii) and not found and not stop:
                if ii[pos] == item:
                    found = True
                else:
                    if ii[pos] > item:
                        stop = True
                    else:
                        pos = pos + 1
            time_end = time.time()
            time_avg.append(float(time_end - time_start))
        time_total_avg.append(statistics.mean(time_avg))
        time_avg = []
    time_total_avg = statistics.mean(time_total_avg)
    return found, time_total_avg


def binary_search_iterative(a_list, item):
    time_avg, time_total_avg = [], []
    first = 0
    last = len(a_list) - 1
    found = False
    for i in a_list:
        for ii in i:
            time_start = time.time()
            while first <= last and not found:
                midpoint = (first + last) // 2
                if ii[midpoint] == item:
                    found = True
                else:
                    if item < ii[midpoint]:
                        last = midpoint - 1
                    else:
                        first = midpoint + 1
            time_end = time.time()
            time_avg.append(float(time_end - time_start))
        time_total_avg.append(statistics.mean(time_avg))
        time_avg = []
    time_total_avg = statistics.mean(time_total_avg)
    return found, time_total_avg


def binary_search_recursive(a_list, item):
    def printresult(time_s, time_a):
        time_end = time.time()
        time_avg.append(float(time_end - time_start))
        return time_avg

    time_avg, time_total_avg = [], []
    for i in a_list:
        for ii in i:
            time_start = time.time()
            if len(ii) == 0:
                time_avg = printresult(time_start, time_avg)
            else:
                midpoint = len(ii) // 2
            if ii[midpoint] == item:
                time_avg = printresult(time_start, time_avg)
            else:
                if item < ii[midpoint]:
                    time_avg = printresult(time_start, time_avg)
                else:
                    time_avg = printresult(time_start, time_avg)
        time_total_avg.append(statistics.mean(time_avg))
        time_avg = []
    time_total_avg = statistics.mean(time_total_avg)
    return None, time_total_avg


def main():
    test_list = list_generator()
    result = sequential_search(test_list, -1)
    print('Sequential Search took {:10.7f} seconds to run, on average'.format(result[1]))

    test_list = sort_list(test_list)

    result = ordered_sequential_search(test_list, -1)
    print('Ordered Sequential Search took {:10.7f} seconds to run, on average'.format(result[1]))

    result = binary_search_iterative(test_list, -1)
    print('Binary Search Iterative took {:10.7f} seconds to run, on average'.format(result[1]))

    result = binary_search_recursive(test_list, -1)
    print('Binary Search Recursive took {:10.7f} seconds to run, on average'.format(result[1]))


main()
