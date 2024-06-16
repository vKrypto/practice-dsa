import functools


class Solution:
    
    def min_energy_to_reach_destination(self, stairs):
        n = len(stairs)
        # base-case
        cache = {
            n-1: 0,
            n-2: abs(stairs[n-1] - stairs[n-2])            
        }
        
        def rec(i):
            if i in cache:
                return cache[i]            
            return min(
                rec(i+1) + abs(stairs[i] - stairs[i+1]),
                rec(i+2) + abs(stairs[i] - stairs[i+2])
            ) 
        
        return rec(0)
    
    
    def min_energy_to_reach_destination_memo(self, stairs):
        n = len(stairs)
        # base-case
        cache = {
            n-1: 0,
            n-2: abs(stairs[n-1] - stairs[n-2])            
        }
        
        def rec(i):
            if i in cache:
                return cache[i]            
            cache[i] = min(
                rec(i+1) + abs(stairs[i] - stairs[i+1]),
                rec(i+2) + abs(stairs[i] - stairs[i+2])
            ) 
            return cache[i]
        
        return rec(0)

print(Solution().min_energy_to_reach_destination([10, 30, 10, 10, 20]))
print(Solution().min_energy_to_reach_destination_memo([10, 30, 10, 10, 20]))
print(Solution().min_energy_to_reach_destination([]))