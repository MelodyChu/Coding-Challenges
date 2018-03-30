# Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.

 # Input:   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
 # Output: [(0, 1), (3, 8), (9, 12)]

def merge_ranges(alist): # list of tuples
#     final_list = set() # want unique time ranges
#     overlaps_set = set()
#     for i in range(0,len(alist)-1):
#         i_start_time = alist[i][0]
#         i_end_time = alist[i][1]
#         for j in range(i+1,len(alist)):
#             j_start_time = alist[j][0]
#             j_end_time = alist[j][1]
#             if not (i_end_time < j_start_time): # end time before start time, don't overlap
#                 overlaps_set.add((min(i_start_time, j_start_time), max(i_end_time, j_end_time)))
#          # they don't overlap
#         final_list.add(alist[i])

#     print overlaps_set

# print merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])

    # build the dictionary
    new_dict = {}
    min_start = alist[0][0]
    max_finish = alist[0][1]
    for time in alist: # start is each tuple
        if time[0] < min_start:
            min_start = time[0]
        if time[1] > max_finish:
            max_finish = time[1]

    for i in range(min_start, max_finish + 1):
        new_dict[i] = 0
    # now we dict :D

    for inc in alist:
        for m in range(inc[0], inc[1]): # 
            new_dict[m] += 1

    print new_dict

# {0: 1, 1: 1, 2: 0, 3: 1, 4: 2, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1, 10: 2, 11: 1, 12: 1}
    in_interval = False
    final_index = 0
    start_index = 0
    overlap_list = []
    for time in new_dict: # e/ a key
        print "time key is " + str(time)
        if in_interval: # if True
            if new_dict[time] == 0:
                in_interval = False
                final_index = time
                print "Final index is " + str(final_index)
                overlap_list.append((start_index, final_index))
                
        else: 
            if new_dict[time] > 0:
                in_interval = True
                start_index = time
                print "Start index is " + str(start_index)
        

    return overlap_list

    


    #return min_start, max_finish
print merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])



