# https://leetcode.com/problems/length-of-last-word/


class Solution {
    public int lengthOfLastWord(String s) {
       List<String> r = Arrays.asList(s.split(" "));
        if (r.size()==0)
            return 0;
        return(r.get(r.size()-1).length());
    }
}