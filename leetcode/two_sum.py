#coding=utf8
__author__ = 'qwy'


class Solution1:
    # @return a tuple, (index1, index2)
    @staticmethod
    def twoSum(num, target):
        # 使用dict缓存所有数据和对应的index，时间复杂度O(n)
        index1 = 0
        index2 = 0
        numberDict = dict()
        for indexCurrent, number in enumerate(num):
            numberDict[number] = indexCurrent
        for indexCurrent, number in enumerate(num):
            diff = target - number
            index2 = numberDict.get(diff, 0)
            if index2 == indexCurrent:
                continue
            if index2:
                index1 = indexCurrent
                break
        return index1 + 1, index2 + 1


class Solution2:
    # @return a tuple, (index1, index2)
    @staticmethod
    def twoSum(num, target):
        # 使用双重循环，时间复杂度O(n^2)
        index1 = 0
        index2 = 0
        bingo = False
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                if target - num[i] == num[j]:
                    index1 = i
                    index2 = j
                    bingo = True
                    break
            if bingo:
                break
        return index1 + 1, index2 + 1


if __name__ == '__main__':
    print 'start two sum'
    num = [1, 2, 3, 4]
    target = 7
    print Solution2.twoSum(num, target)
    print 'finished two sum'


class Solution_others:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        map = {}  # maps element to its index
        for i in range(len(num)):
            if target - num[i] in map:
                i1 = i + 1
                i2 = map[target - num[i]] + 1
                return (min(i1, i2), max(i1, i2))
            else:
                map[num[i]] = i
