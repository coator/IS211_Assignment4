import time
import statistics
import random


def insertion_sort(a_list):
    time_avg, time_total_avg = [], []
    for i in a_list:
        for ii in i:
            time_start = time.time()
            for index in range(1, len(ii)):
                current_value = ii[index]
                position = index
                while position > 0 and ii[position - 1] > current_value:
                    ii[position] = ii[position - 1]
                    position = position - 1
                    ii[position] = current_value
            time_end = time.time()
            time_avg.append(float(time_end - time_start))
        time_total_avg.append(statistics.mean(time_avg))
    time_total_avg = statistics.mean(time_total_avg)
    return time_total_avg


def shell_sort(a_list):
    def gap_insertion_sort(a_list, start, gap):
        for i in range(start + gap, len(a_list), gap):
            current_value = a_list[i]
            position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value

    time_avg, time_total_avg = [], []
    for i in a_list:
        for ii in i:
            time_start = time.time()
            sublist_count = len(ii) // 2
            while sublist_count > 0:
                for start_position in range(sublist_count):
                    gap_insertion_sort(ii, start_position, sublist_count)

                # print("After increments of size", sublist_count, "The list is", ii)
                sublist_count = sublist_count // 2
            time_end = time.time()
            time_avg.append(float(time_end - time_start))
        time_total_avg.append(statistics.mean(time_avg))
    time_total_avg = statistics.mean(time_total_avg)
    return time_total_avg


def python_sort(a_list):
    time_avg, time_total_avg = [], []
    for i in a_list:
        for ii in i:
            time_start = time.time()
            ii.sort()
            time_end = time.time()
            time_avg.append(float(time_end - time_start))
        time_total_avg.append(statistics.mean(time_avg))
    time_total_avg = statistics.mean(time_total_avg)
    return time_total_avg


def list_generator():
    list500 = [random.choices(range(1, 101), k=500) for num in range(100)]
    list1000 = [random.choices(range(1, 101), k=1000) for num in range(100)]
    list10000 = [random.choices(range(1, 101), k=10000) for num in range(100)]
    return list500, list1000, list10000


def main():
    test_list = list_generator()
    test_lista, test_listb, test_listc = test_list,test_list,test_list
    result = shell_sort(test_lista)
    print('Shell Sort took {:10.7f} seconds to run, on average'.format(result))
    result = python_sort(test_listb)
    print('Python Sort took {:10.7f} seconds to run, on average'.format(result))
    result = insertion_sort(test_listc)
    print('Insertion Sort took {:10.7f} seconds to run, on average'.format(result))


main()
