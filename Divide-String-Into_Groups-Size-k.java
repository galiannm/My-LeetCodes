class Solution {
    public String[] divideString(String s, int k, char fill) {
        int n = s.length();
        int num_groups = (n + k - 1) / k;
        String[] res = new String[num_groups];
        for (int i = 0; i < num_groups; i++) {
            int start = i * k;
            int end = Math.min((i*k) + k, n);
            String group = s.substring(start, end);

            if (end - start < k) {
                group += String.valueOf(fill).repeat(k-(end-start));
            }
            res[i] = group;
        }
        return res;
    }
}