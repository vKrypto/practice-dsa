from typing import List
import sys

class Solution:
    def can_reach_destination(self, trackLength, spells, k):
        total_distance = 0
        speed = 0
        last_spell_time = 0
        for spell_time in spells + [sys.maxsize]:
            time_passed_from_last_spell = max(spell_time - last_spell_time, 0)
            last_spell_time = spell_time
            distance_covered = 0
            temp_speed = speed
            for _ in range(time_passed_from_last_spell):
                distance_covered += temp_speed
                temp_speed -= 1    
                if temp_speed == 0:
                    break
            print("distance_covered", distance_covered)
            total_distance += distance_covered
            speed = max(k, speed-time_passed_from_last_spell)
            if total_distance >= trackLength:
                break
        return total_distance >= trackLength
    
    def minimizeTopSpeed(self, n :int, spells : List[int], trackLength:int) -> int:
        left = 1 
        right = max(spells) 
        
        while left < right:
            mid = left + (right - left) // 2
            # mid = 8
            can_reach = self.can_reach_destination(trackLength, spells, mid)
            print(mid, can_reach)
            # break
        
            if can_reach:
                right = mid
            else:
                left = mid + 1
    
        return left
        

        

# Example usage:
trackLength = 29
spells = [2, 14]
result = Solution().minimizeTopSpeed(5, spells, trackLength)
print("Minimum value of k required:", result)


class GeekTraveler:
    def find_minimum_k(self, track_length, n, spells):
        left = 1
        right = track_length

        while left < right:
            mid = (left + right) // 2

            total_speed = 0
            for spell_time in spells:
                total_speed += min(mid, spell_time)

            if total_speed >= track_length:
                right = mid
            else:
                left = mid + 1

        return left

# Test case
trackLength = 20
n = 3
spells = [1, 5, 9]

geek_traveler = GeekTraveler()
minimum_k = geek_traveler.find_minimum_k(trackLength, n, spells)
print(minimum_k)  # Output: 6