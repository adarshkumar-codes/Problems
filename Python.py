# 2833. Furthest Point From Origin
# Solved
# https://leetcode.com/problems/furthest-point-from-origin/
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        a = moves.count('L')
        b = moves.count('R')
        c = moves.count('_')
        return max(a+c-b,b+c-a)

