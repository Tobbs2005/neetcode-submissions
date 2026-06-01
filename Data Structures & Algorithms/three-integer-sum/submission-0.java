class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Map<Integer, List<int[]>> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            for(int j = i+1; j < nums.length; j++){
                
                int sum = nums[i] + nums[j];
                map.putIfAbsent(sum, new ArrayList<>());
                map.get(sum).add(new int[]{i, j});


            }
        }

        List<List<Integer>> res = new ArrayList<>();
        Set<List<Integer>> uniq = new HashSet<>();
        for(int k=0; k < nums.length; k++){
            int need = -nums[k];
            List<int[]> pairs = map.get(need);
            if (pairs == null) continue;

            for(int[] p: pairs){
                int i = p[0];
                int j = p[1];
                if (i == k || j == k) continue;
                int[] t = new int[]{nums[i], nums[j], nums[k]};

                //dedupe
                Arrays.sort(t);
                uniq.add(Arrays.asList(t[0], t[1], t[2]));

            }
        }
        return new ArrayList<>(uniq);
    }
}
