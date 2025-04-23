class Solution:
    def subsets(self,nums:List[int]) -> List[List[int]]:
        def dfs(nums,index,path,ans):
            ans.append(path)
            [dfs(nums,i+1,path+[nums[i]],ans) for i in range(index,len(nums))]
        ans=[]
        dfs(nums,0,[],ans)
        return ans