class Solution(object):
    def heightChecker(self, heights):
        # Make a sorted copy
        expected = sorted(heights)
        
        # Count mismatches
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        
        return count
heights = list(map(int, input("Enter numbers (comma-separated): ").split(",")))

sol = Solution()
print(sol.heightChecker(heights))