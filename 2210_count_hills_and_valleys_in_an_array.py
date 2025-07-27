class Solution:
    def countHillValley(self, nums: List[int]) -> int:
#          let n=|nums|
# set prev=nums[0], cnt=0
# define boolean array diff[2]={0, 0}
# Proceed a nested loop as follows
        n, prev, cnt=len(nums), nums[0], 0
        diff=[0, 0]
        i=0
        while i<n:
            while i<n and prev==nums[i]: i+=1
            if i==n: break
            bigger=1 if nums[i]>prev else 0
            diff[bigger]=1
            cnt+=diff[bigger] and diff[1-bigger]
            diff[1-bigger]=0
            prev=nums[i]
            i+=1
        return cnt

       