# https://leetcode.com/problems/combination-sum/description/
from typing import List
from time import perf_counter
import timeit



class Solution:
    # time: o(n*n), space: o(N)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def dfs(total=0, index=0):
            if total == target:
                res.append(cur.copy())
                return
            elif total > target:
                return

            for i in range(index, len(candidates)):
                cur.append(candidates[i])
                dfs(total+candidates[i], i)
                cur.pop()
        dfs()

        return res
    
    # time: o(2*n), space: o(n)
    def combinationSum_optimized(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

#T: O(2^T)
#S: O(N)

class Solution2:
    
    # TLE o(target*n), recursive.
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        steps = [0]
        dp = [0]* (target + 1)
        dp[target] = 1
        def dfs(sum_yet=0):
            print(sum_yet, )
            res = 0
            for i in nums:
                steps[0] += 1
                if sum_yet + i > target:
                    break
                if dp[sum_yet + i]:
                    res += dp[sum_yet + i]
                else:
                    res += dfs(sum_yet + i)
            dp[sum_yet] = res
            return res
        return dfs()
    
    def combinationSum4_2(self, nums: List[int], target: int) -> int:
        dp = {}
        dp[0] = [1]

        def search(target):
            if target in dp:
                return dp[target]
            comb_sum = 0
            for num in nums:
                if target > num:
                    comb_sum += search(target - num)
                elif target == num:
                    comb_sum += 1
            dp[target] = comb_sum
            return comb_sum

        return search(target)



tests = [
    [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700,710,720,730,740,750,760,770,780,790,800,810,820,830,840,850,860,870,880,890,900,910,920,930,940,950,960,970,980,990,111],
]


t3 = perf_counter()
Solution2().combinationSum4_2(tests[0], 999)
t4 = perf_counter()
print(f" total time took {t4-t3}")


t1 = perf_counter()
Solution2().combinationSum4(tests[0], 999)
t2 = perf_counter()

print(f" total time took {t2-t1}")