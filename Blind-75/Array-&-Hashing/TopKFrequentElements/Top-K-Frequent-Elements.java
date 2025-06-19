import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    class pair{
        int first;
        int second;
        pair(int first, int second) {
            this.first = first;
            this.second = second;
        }
    }
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> countNums = new HashMap<>();

        // count frequency
        for (int i = 0; i < nums.length; i++){
            countNums.put(nums[i], countNums.getOrDefault(nums[i], 0) + 1);
        }
        
        // create priority queue (max)
        PriorityQueue<pair> pq = new PriorityQueue<>((a, b)-> (b.first - a.first)); // heap order by highest freq (b-a -> to reverse order because java default is min ordered)
        for (Map.Entry<Integer, Integer> it : countNums.entrySet())
            pq.add(new pair(it.getValue(), it.getKey()));
        
        int[] res = new int[k];
        int i = 0;
        while (k-- > 0 && pq.size() > 0){
            int top = pq.peek().second;
            pq.poll();
            res[i++] = top;
        }
        return res;
    }
}