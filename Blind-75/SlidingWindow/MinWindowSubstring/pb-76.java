import java.util.*;
class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) return "";
        HashMap<Character, Integer> mapT = new HashMap<>();
        HashMap<Character, Integer> window = new HashMap<>();
        String res = ""; int lengthRes = Integer.MAX_VALUE;
        for (int i = 0; i < t.length(); i++){
            mapT.put(t.charAt(i), mapT.getOrDefault(t.charAt(i), 0) + 1);
        }
        int need = mapT.size(); int have = 0;
        int l = 0;
        for (int r = 0; r < s.length(); r++){
            char c = s.charAt(r);
            if (mapT.containsKey(c)){
                window.put(c, window.getOrDefault(c, 0)+1);
                if (window.get(c).equals(mapT.get(c))) have++;
            }    
            while (have == need){
                if ((r-l+1) < lengthRes){
                    lengthRes = r-l+1;
                    res = s.substring(l,r+1);
                }
                char leftChar = s.charAt(l);
                if (mapT.containsKey(leftChar)) {
                    window.put(leftChar, window.get(leftChar) - 1);
                    if (window.get(leftChar) < mapT.get(leftChar)) {
                        have--;
                    }
                }
                l++;
            }
        }
        return res;
    }
}