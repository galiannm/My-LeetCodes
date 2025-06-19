import java.util.HashSet;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        int res = 0;
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) { set.add(num);}

        for (int num : nums){
            int count = 0;
            if (!set.contains(num-1)){
                while (set.contains(num++))
                    count += 1;
            }
            res = Math.max(res, count);
        }
        return res;
    }
}