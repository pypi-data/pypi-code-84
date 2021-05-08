'''
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The 
bricks have the same height but different width. You want to draw a vertical line from the top to the 
bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width 
of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to 
find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will 
obviously cross no bricks.

Example:
Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2
'''
from collections import Counter

def least_bricks(wall):
    #count = collections.Counter()
    count = Counter()
    for row in wall:
        for i in range(1, len(row)):
            row[i] += row[i - 1]
            count[row[i - 1]] += 1

    return len(wall) if not count else len(wall) - count.most_common(1)[0][1]
