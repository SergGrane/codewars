# Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.
#
# Intervals
# Intervals are represented by a pair of integers in the form of an array.
# The first value of the interval will always be less than the second value.
# Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
def sum_of_intervals(intervals):
    intervals.sort()
    b, e, s = 0, 0, 0
    print(intervals)

    for begin, end in intervals:
        #if begin * end > 0:
        #    s += abs(abs(begin) - abs(end))
        if b < begin < e or b < end < e or e != 0 and b != 0:
            s = s - abs(e)-abs(b) + abs(max(e, end) - min(b, begin))

        else:
            s += abs(end) + abs(begin)
            print('sssss', s)

 #       if b < begin < e or b < end < e or e!=0 and b!=0 :
 #           s = s - abs(e)-abs(b) + abs(max(e, end) - min(b, begin))
#        elif b == begin and end == e:
 #           s += 0
 #       elif  e !=0 and b !=0:
 #       else:
  #          s += abs(end) - abs(begin)
        b, e = begin, end
        print(s)

    return s


if __name__ == '__main__':
    print(sum_of_intervals([(1, 5), (6, 10)]))