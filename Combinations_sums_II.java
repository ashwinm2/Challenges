# Combinations sums II
public class Solution {
    Set<List<Integer>> full = new HashSet<List<Integer>>();
    
    public void compute(List<Integer> branch, int[] nums ,int target)
    {
        if(target == 0)
        {
            Collections.sort(branch);
            full.add(branch);
        }
        else
        {
            while(nums != null && target - nums[0] >= 0)
            {
                if(nums.length > 1)
                {
                    List<Integer> node = new ArrayList<Integer>(branch);
                    int temp = nums[0];
                    node.add(temp);
                    nums = Arrays.copyOfRange(nums, 1, nums.length);
                    compute(node, nums, target - temp);    
                }
                else
                {
                    if(target - nums[0] == 0)
                    {   
                        List<Integer> node = new ArrayList<Integer>(branch);
                        node.add(nums[0]);
                        Collections.sort(node);
                        full.add(node);
                    }
                    nums = null;
                }
            }
        }
        
    }
    
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        if(candidates.length != 0)
        {
            Arrays.sort(candidates);
            while(candidates != null)
            {
                List<Integer> node = new ArrayList<Integer>();
                int temp = candidates[0];
                if(candidates.length > 1)
                {   
                    node.add(temp);
                    candidates = Arrays.copyOfRange(candidates, 1, candidates.length);
                    compute(node, candidates, target - temp);
                }
                else
                {
                    if(temp == target)
                    {
                        node.add(temp);
                        full.add(node);
                    }
                    candidates = null;   
                }
                
            }
        }
        List<List<Integer>> list = new ArrayList<List<Integer>>(full);
        return list;
    }
}