class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] countAlph = new int[26];
        for (int i = 0; i < s.length(); i++){
            char c1 = s.charAt(i);
            char c2 = t.charAt(i);
            countAlph[c1 - 'a'] += 1;
            countAlph[c2 - 'a'] -= 1;
        }
        for (int i = 0; i < countAlph.length; i++){
            if (countAlph[i] != 0) return false;
        }
        return true;
    }
}