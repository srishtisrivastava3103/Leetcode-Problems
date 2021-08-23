# https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1/?category[]=Dynamic%20Programming&category[]=Dynamic%20Programming&page=4&query=category[]Dynamic%20Programmingpage4category[]Dynamic%20Programming#

def subsetSum(nums,s,i,currsum):
    if currsum==0:
        return True
    if i>=len(nums) or currsum<0:
        return False
    if nums[i]>currsum:
        return subsetSum(nums,s,i+1,currsum)
    if nums[i]<=currsum:
        return subsetSum(nums,s,i+1,currsum-nums[i]) or subsetSum(nums,s,i+1,currsum)
subsetSum([3, 34, 4, 12, 5,2],30,0,30)