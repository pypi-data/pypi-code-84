'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite 
restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a 
hoice tie between answers, output all of them with no order requirement. You could assume there always 
exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
'''
import sys
def minimum_lists(list1, list2):
    list1_map = {restaurant:index for index, restaurant in enumerate(list1)}
    result = []
    min_index_sum = sys.maxsize
    for index, restaurant in enumerate(list2):
        if restaurant in list1_map:
            index_sum = index + list1_map[restaurant]
            if index_sum < min_index_sum:
                result = [restaurant]
                min_index_sum = index_sum
            elif min_index_sum == index_sum:
                result.append(restaurant)
    return result

