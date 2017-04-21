# Combinations sums
public class Solution {
    Set<List<Integer>> full = new HashSet<List<Integer>>();
    
    public void compute(List<Integer> branch, int[] nums ,int target)
    {
        if(target > 0)
        {
            int index = 0;
            while(index < nums.length)
            {
                if(target - nums[index] >= 0)
                {
                    List<Integer> node = new ArrayList<Integer>(branch);
                    node.add(nums[index]);
                    compute(node, nums, target - nums[index]);    
                }
                else
                {
                    index = nums.length;
                }
                index += 1;
            }
        }
        else if(target == 0)
        {
            Collections.sort(branch);
            full.add(branch);
        }
    }
    
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        if(candidates.length != 0)
        {
            Arrays.sort(candidates);
            while(candidates != null)
            {
                List<Integer> node = new ArrayList<Integer>();
                node.add(candidates[0]);
                compute(node, candidates, target - candidates[0]);
                if(candidates.length > 1)
                {
                    candidates = Arrays.copyOfRange(candidates, 1, candidates.length);
                }
                else
                {
                    candidates = null;   
                }
            }
            
            Iterator iter = full.iterator();
            while (iter.hasNext()) {
                List<Integer> temp = (List<Integer>)iter.next();
                
                for(int index = 0; index < temp.size(); index++)
                {
                    System.out.print(temp.get(index) + " ");
                }
                System.out.println("");
            }
            
        }
        List<List<Integer>> list = new ArrayList<List<Integer>>(full);
        return list;
    }
}