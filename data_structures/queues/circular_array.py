class CQ:
    
    def __init__(self, n) -> None:
        self.n = n
        self.front = n//3
        self.data = list(range(n))
        
    
    def traverse(self):
        i = j = self.front
        print(i, j, self.data[i], self.data[j])

        while True:
            if (i == j != self.front):
                break
            i -= 1
            if i == -1:
                i += self.n

            j += 1
            if j >= self.n:
                j -= self.n
            
            print(i, j, self.data[i], self.data[j])
            
        
CQ(10).traverse()