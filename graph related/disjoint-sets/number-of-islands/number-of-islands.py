
class Solution:
    def numIslands(self, grid):
        ans=0
        return ans



x =[["1",".",".","1","1","1",".","1","1",".",".",".",".",".",".",".",".",".",".","."],["1",".",".","1","1",".",".","1",".",".",".","1",".","1",".","1",".",".","1","."],[".",".",".","1","1","1","1",".","1",".","1","1",".",".",".",".","1",".","1","."],[".",".",".","1","1",".",".","1",".",".",".","1","1","1",".",".","1",".",".","1"],[".",".",".",".",".",".",".","1","1","1",".",".",".",".",".",".",".",".",".","."],["1",".",".",".",".","1",".","1",".","1","1",".",".",".",".",".",".","1",".","1"],[".",".",".","1",".",".",".","1",".","1",".","1",".","1",".","1",".","1",".","1"],[".",".",".","1",".","1",".",".","1","1",".","1",".","1","1",".","1","1","1","."],[".",".",".",".","1",".",".","1","1",".",".",".",".","1",".",".",".","1",".","1"],[".",".","1",".",".","1",".",".",".",".",".","1",".",".","1",".",".",".","1","."],["1",".",".","1",".",".",".",".",".",".",".","1",".",".","1",".","1",".","1","."],[".","1",".",".",".","1",".","1",".","1","1",".","1","1","1",".","1","1",".","."],["1","1",".","1",".",".",".",".","1",".",".",".",".",".",".","1",".",".",".","1"],[".","1",".",".","1","1","1",".",".",".","1","1","1","1","1",".","1",".",".","."],[".",".","1","1","1",".",".",".","1","1",".",".",".","1",".","1",".",".",".","."],["1",".",".","1",".","1",".",".",".",".","1",".",".",".","1",".","1",".","1","1"],["1",".","1",".",".",".",".",".",".","1",".",".",".","1",".","1",".",".",".","."],[".","1","1",".",".",".","1","1","1",".","1",".","1",".","1","1","1","1",".","."],[".","1",".",".",".",".","1","1",".",".","1",".","1",".",".","1",".",".","1","1"],[".",".",".",".",".",".","1","1","1","1",".","1",".",".",".","1","1",".",".","."]]

for l in x:
    print(l)


    [["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"],["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"],["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"],["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"],["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"],["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"],["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"],["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"],["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"],["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"],["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"],["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"],["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"],["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"],["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"],["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"],["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"],["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"],["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]]



    
    
class Solution:
        
    def numIslands(self, grid: List[List[str]]) -> int:
        components = []
        count = -1
        sub = []
        for r in range(len(grid)):
            prev = "0"
            for i in range(len(grid[r])):
                above = "0" if r == 0 else grid[r-1][i]
                cur = grid[r][i]
                if (cur == "1"):
                    if (prev == "0" and above == "0"):  
                        count+=1
                        components.append(count)
                        grid[r][i] = count
                    if (above != "0"):
                        grid[r][i] = components[above]
                        if (r == 18 and i == 7):
                            print(above, components[above])
                    if (prev != "0"):
                        if (grid[r][i] != "1"):
                            #union
                            components[prev] = components[grid[r][i]] 
                            if (prev != grid[r][i]):
                                count-=1
                                if (r == 18 and i == 7):
                                    print(grid[r-2])
                                    print(grid[r-1])
                                    print(grid[r])
                        else:
                            grid[r][i] = components[prev]
                    
                                    
                prev = grid[r][i]
        return count + 1
    