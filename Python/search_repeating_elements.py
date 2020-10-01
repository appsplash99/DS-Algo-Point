""" APPROACH: 
    1. Over each iteration get the positive value of element at index i;
    2. if list element at index(= abs(nums[i])) is positive, make it negative;
    3. if its negative, append its absolute value into dupes list.

    Efficiency :
    Time Complexity - O(n)
    Space Complexity - O(n)
"""
def search_dups(nums): 
    """ returns None

        attributes- nums(int/float)
    """
    print("Repeating Elements are: ", end="")
    
    for i in range(len(nums)):                  # iterating from 0 to n-1
        
        if nums[abs(nums[i])] >= 0:                    # only positive elements
            nums[abs(nums[i])] = -nums[abs(nums[i])]   # at index val assign a negative element within the nums list
        else:                                          
            print(abs(nums[i]), end=' ')


# code within the below if block only executes within this module.
if __name__ == '__main__':
    nums = [1, 2, 3, 1, 3, 6, 6]                # Repeating Elements:  1 3 6 
    search_dups(nums)




