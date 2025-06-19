import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // [-4,-1,-1,0,1,2] -> (-1,-1,2) (-1,0,1)
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        for (int i = 0; i < nums.length; i++){
            // do not want to repet patterns
            if (i > 0 && nums[i-1] == nums[i]) continue;
            int l = i + 1; int r = nums.length-1;
            while (l < r){
                int threeSum = nums[i] + nums[l] + nums[r];
                if (threeSum == 0){
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    // do not want to repeat patterns
                    do {l++;}
                    while (nums[l-1] == nums[l] && l < r);
                } else if (threeSum < 0){
                    l++;
                } else {
                    r --;
                }
            }
        }
        return res;
    }
}