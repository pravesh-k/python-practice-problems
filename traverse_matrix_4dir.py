from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        row = len(image)
        col = len(image[0])
        old_color = image[sr][sc]

        def traverse(i, j):
            
            nonlocal row, col, old_color, image, newColor

            if image[i][j]!=old_color or i>0 or i<row-1 or j>0 or j<col-1:
                return

            image[i][j] = newColor
            
            traverse(i+1, j)
            traverse(i-1, j)
            traverse(i, j+1)
            traverse(i, j-1)
        
        traverse(sr, sc)

        return image


# driver code
def main():

    sol = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2

    print(sol.floodFill(image, sr, sc, newColor))


if __name__ == "__main__":
    main()
