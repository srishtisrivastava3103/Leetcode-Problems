# https://leetcode.com/problems/best-sightseeing-pair/


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        left = values[0]
        best_score = float('-inf')
        for v in values[1:]:
            best_score = max(best_score, left + v - 1)
            left = max(left - 1, v)
        return best_score
