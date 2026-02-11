def threeSumSmaller(self, nums, target):
    # Initialize result
    n = len(nums)
    ans = 0

    # Fix the first element as A[i]
    for i in range( 0 ,n-2):
    
        # Fix the second element as A[j]
        for j in range( i+1 ,n-1):
    
            # Now look for the third number
            for k in range( j+1, n):
                if (nums[i] + nums[j] + nums[k] < target):
                    ans+=1
    
    return ans

sample_arr = [-10, -8, -3, 1, 5]
tar = -5
ans = threeSumSmaller(sample_arr, tar)
print(ans)