
class Solution:
    def uniquePositions(self, moves : str, k : int) -> int:
        # code here
        positions = set()
        positions.add(0)
        position = 0
        
        for move in moves:
            if move == 'F':
                position += 2
            else:
                position -= 2
            if position not in positions:
                positions.add(position)
                
            
        return len(positions)
    
    
print(Solution().uniquePositions("FFFF", 1))