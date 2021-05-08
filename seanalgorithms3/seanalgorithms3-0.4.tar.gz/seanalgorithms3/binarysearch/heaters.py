'''
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm 
radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of 
heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will 
be the minimum radius standard of heaters.

Note:

Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
 

Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all 
the houses can be warmed.
 

Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all 
the houses can be warmed.
'''

def heaters(houses, heaters):
    
    def search(x):
        left, right = 0, len(heaters) - 1
        while left + 1 < right: 
            mid = (left + right) // 2
            if heaters[mid] == x:
                return [heaters[mid]]
            elif heaters[mid] < x:
                left = mid
            else:
                right = mid

        return [heaters[left], heaters[right]]
    
    heaters = [float('-inf')] + heaters + [float('inf')]
    heaters.sort()

    radius = 0
    for house in houses:
        position = search(house)
        if len(position) == 2:
            left, right = position 
            min_heater_dist = min(abs(left - house), abs(right - house))
            radius = max(radius, min_heater_dist)

    return radius 