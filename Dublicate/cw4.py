# Given a set of numbers, return the additive inverse of each.
# Each positive becomes negatives, and the negatives become positives.
#
# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.
# lst = [1,-2,6,-4,5]
# neg_list = []
# def invert(lst):
#     for i in lst:
#          neg_list.append(-1 * (i))
#     return [-x for x in lst]
# print(invert(lst))
#  return [-x for x in lst]