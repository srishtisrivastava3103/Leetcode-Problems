# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        down = 1
        row = 0
        arr = [""]*(numRows)
        if numRows==1:
            return s
    
        for i in range(len(s)):
            arr[row]+=s[i]
            if row==numRows-1:
                down = -1
            if row==0:
                down = 1
            if down==1:
                row+=1
            else:
                row-=1
        return ''.join(arr)
