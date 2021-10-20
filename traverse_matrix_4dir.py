## This problem is from LeetCode numbered #733. Flood Fill

# Problem Statement: An image is represented by an m x n integer grid image 
# where image[i][j] represents the pixel value of the image. You are also given 
# three integers sr, sc, and newColor. You should perform a flood fill on the 
# image starting from the pixel image[sr][sc]. To perform a flood fill, consider 
# the starting pixel, plus any pixels connected 4-directionally (up, down, left, 
# right) to the starting pixel of the same color as the starting pixel, plus any 
# pixels connected 4-directionally to those pixels (also with the same color), 
# and so on. Replace the color of all of the aforementioned pixels with newColor. 
# Return the modified image after performing the flood fill.

# Costraints:
# row == image.length
# col == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], newColor < 2^16
# 0 <= sr < m
# 0 <= sc < n


from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        row = len(image)                # number of rows of the image matrix
        col = len(image[0])             # number of rows of the image matrix
        old_color = image[sr][sc]       # variable indicating the original color that 
                                        # needs to be changed when conditions met

        # recursive function to perform DFS starting from image[sr, sc]
        def traverse(i, j):
            
            nonlocal row, col, old_color, image, newColor       # declaring the variables non-local to
                                                                # use the variable from parent function

            # when not to change the colour of the pixel
            if i<0 or i>row-1 or j<0 or j>col-1 or image[i][j]!=old_color or image[i][j] == newColor:
                return

            # when conditions satisfied for changing the color, perform color change
            image[i][j] = newColor

            # recursilvely perform the same color change operation on the 
            # neigbours lying in the 4 directions(up, down, left, right)

            traverse(i+1, j)        # down
            traverse(i-1, j)        # up
            traverse(i, j+1)        # right
            traverse(i, j-1)        # left
        
        # calling the recursive traverse function
        traverse(sr, sc)

        return image


# driver code
def main():

    sol = Solution()
    image = [[0,0,0],[0,1,1]]
    sr = 1
    sc = 1
    newColor = 1

    print(sol.floodFill(image, sr, sc, newColor))


if __name__ == "__main__":
    main()
