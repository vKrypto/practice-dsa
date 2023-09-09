

class Solution:
    def canCompleteTrack(self, tracklength, spells, mid):
        n = len(spells)
        for i in range(n):
            if i < n-1:
                k = spells[i+1] - spells[i]
                if k >= mid:
                    dis = (((mid)*(mid+1))/2)
                else:
                    dis = (k * mid) - (k*(k-1))/2
            else:
                dis = ((mid)*(mid+1))/2
            tracklength -= dis
            if tracklength <= 0:
                return True
        return False
        
                
    def minimizeTopSpeed(self, n , spells , tracklength) -> int:
        spells.sort()
        low = 1
        high = tracklength
        ans = tracklength
        while low <= high:
            mid = low + (high - low)//2
            if self.canCompleteTrack(tracklength, spells, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        
