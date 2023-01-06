# What if we need the length of the words separated by a
# space to be added at the end of that same word and have it returned as an array?
# apple_ban = ('you will win')
# neg_list = []
# def invert(lst):
#     for i in lst.split(' '):
#         neg_list.append(i + ' ' + str(len(i)))
#     return neg_list
# print(invert(apple_ban))
# print(apple_ban.split(' '))
#Better version
def add_length(str_):
    return ["{} {}".format(i, len(i)) for i in str_.split(' ')]