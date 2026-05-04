# 796. Rotate String
# https://leetcode.com/problems/rotate-string/description/
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i = 0
        while i <= len(s):
            if s[i:]+s[:i] == goal:
                return True
            i+=1
        return False


# 2833. Furthest Point From Origin
# Solved
# https://leetcode.com/problems/furthest-point-from-origin/
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        a = moves.count('L')
        b = moves.count('R')
        c = moves.count('_')
        return max(a+c-b,b+c-a)

# 367. Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/

import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return math.sqrt(num) % 1 == 0
