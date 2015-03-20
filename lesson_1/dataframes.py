from pandas import DataFrame, Series

'''
Just the first example from the lesson.
'''
data_frame_src = {
    'name': Series(['Braund', 'Cummings', 'Heikkinen', 'Allen'], index=['a', 'b', 'c', 'd']),
    'age': Series([22, 38, 26, 35], index=['a', 'b', 'c', 'd']),
    'fare': Series([7.25, 71.83, 8.05], index=['a', 'b', 'd']),
    'survived': Series([False, True, True, True], index=['a', 'b', 'c', 'd'])
}

frame = DataFrame(data_frame_src)

if __name__ == '__main__':
    print(frame)
