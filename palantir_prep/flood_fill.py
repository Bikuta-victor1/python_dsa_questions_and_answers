from typing import List


class Solution:
        # Dfs Util function
    def dfs(self, image: List[List[int]], sr: int, sc: int, color: int, source : int ):

        # Check if the present color is beyond boundaries o
        if sr < 0 or sr > len(image)-1 or sc < 0 or sc > len(image[0])-1 or image[sr][sc] != source:
            return
        
        # Changing color of recursed value to new color 
        image[sr][sc] = color
        
       # Recursion for the four directions
        self.dfs(image, sr, sc+1, color, source )
        self.dfs(image, sr, sc-1, color, source )
        self.dfs(image, sr+1, sc, color, source )
        self.dfs(image, sr-1, sc, color, source )


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # if the color matches the image already we return the image
        if color == image[sr][sc]:
            return image

        # Get size of rows and colums and value of initial source color
        source = image[sr][sc]

        # do dfs for initial source
        self.dfs(image, sr, sc, color, source)

        return image
        
