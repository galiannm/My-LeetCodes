import java.util.Hashtable; 
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Hashtable<Integer, Integer> t = new Hashtable<>();
        for (int i = 0; i < nums.length; i++){
            if (t.containsKey(target-nums[i])){
                return new int[]{i, t.get(target-nums[i])};
            } 
            t.put(nums[i], i);
        }
        return new int[]{};
    }
}