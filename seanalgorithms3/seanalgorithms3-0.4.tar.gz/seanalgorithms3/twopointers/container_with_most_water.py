'''
Given n non-negative integers a1, a2, ..., an , where each 
represents a point at coordinate (i, ai). n vertical lines 
are drawn such that the two endpoints of line i is at (i, ai)
 and (i, 0). Find two lines, which together with x-axis forms 
 a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can 
contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

'''

def max_area_water(heights) -> int:
    left, right = 0, len(heights)-1
    max_area = 0

    while left < right:
        area = (right-left) * min(heights[left], heights[right])
        if area > max_area:
            max_area = area
        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
    return max_area

