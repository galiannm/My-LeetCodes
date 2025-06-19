class Solution {
    // O(N)
    public int maxProfit(int[] prices) {
        int res = 0;
        int l = 0;
        for (int r = 0; r < prices.length; r++){
            while(prices[r] - prices[l] < 0) l++;
            res = Math.max(res, prices[r] - prices[l]);
        }
        return res;
    }
}