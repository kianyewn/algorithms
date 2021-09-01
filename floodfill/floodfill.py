class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        visited = [[False]* len(image[0]) for _ in range(len(image))]
        # print(visited)
        return self.dfs(image, sr,sc, newColor, visited)
    
    def dfs(self, image, sr, sc, newColor, visited):
        if not visited[sr][sc]:
            visited[sr][sc] = True
            current_color = image[sr][sc]
            image[sr][sc] = newColor
            if (sr+1 < len(image)) and (image[sr+1][sc] == current_color):
                move_up = self.dfs(image, sr+1, sc, newColor, visited)
            if  (sr-1 >= 0) and (image[sr-1][sc] == current_color):
                move_down = self.dfs(image, sr-1, sc, newColor, visited)
            if (sc-1 >= 0) and (image[sr][sc-1] == current_color):
                move_left = self.dfs(image, sr, sc-1, newColor, visited)
            if (sc+1 <len(image[0])) and (image[sr][sc+1] == current_color):
                move_right = self.dfs(image, sr, sc+1, newColor, visited)
        return image
        
        