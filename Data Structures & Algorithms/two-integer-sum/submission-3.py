class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        res = []
        for i, num in enumerate(nums):
            if target - num in freq:
                res.append(i)
                res.append(freq[target - num])
                break
            else:
                freq[num] = i
        return sorted(res)
        