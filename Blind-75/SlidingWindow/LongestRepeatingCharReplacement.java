import java.util.*;
class Solution {
    // O(N)
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> freq = new HashMap<>();
        int res = 0;
        int l = 0;
        int maxFreq = 0;
        for (int r = 0; r < s.length(); r++){
            char c = s.charAt(r);
            freq.put(c, freq.getOrDefault(c, 0)+1);
            maxFreq = Math.max(maxFreq, freq.get(c));
            while ((r-l+1) - maxFreq > k){ 
                freq.put(s.charAt(l), freq.get(s.charAt(l)) - 1);
                l++;
            }
            res = Math.max(res, r-l+1);
        }
        return res;
    }
}