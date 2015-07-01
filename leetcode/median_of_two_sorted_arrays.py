#codi=utf-8
__author__ = 'qwy'


class Solution1:
    # @return a float
    @staticmethod
    def findMedianSortedArrays(A, B):
        C = sorted(A + B)
        # print C
        if len(C) % 2 == 0:
            index = len(C) / 2
            median = (C[index] + C[index - 1]) / 2.0
        else:
            index = (len(C) - 1) / 2
            median = C[index]
        return median

    @staticmethod
    def find_median_in_sorted_array(C):
        if len(C) % 2 == 0:
            index = len(C) / 2
            median = (C[index] + C[index - 1]) / 2.0
        else:
            index = (len(C) - 1) / 2
            median = C[index]
        return median

if __name__ == '__main__':
    print 'start findMedianSortedArrays'
    array_a = [1, 2, 3, 4]
    array_b = [1, 2, 99, 100, 101]
    array_e = [1]
    print Solution1.findMedianSortedArrays(array_a, array_b)
    print 'finished findMedianSortedArrays'