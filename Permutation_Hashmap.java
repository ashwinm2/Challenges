// Permutation Hashmap
import java.lang.Math; 
import java.util.*;

public class HelloWorld
{
  
  public static void main(String[] args)
  {
    int[] arr = {1,2,3,4};
    Solution obj = new Solution();
    
    arr = obj.nextPermutation(arr);
    
    for(int i = 0; i < arr.length; i++)
    {
     	System.out.print(arr[i]); 
  	}
  }
}




public class Solution {
    public int[] nextPermutation(int[] nums) 
    {
        int prev = Integer.MIN_VALUE;
        int index = nums.length - 1;
        while(index >= 0)
        {
            if(prev > nums[index])
            {
                int length = nums.length;
                Map<Integer, Grouping> dict = compute(nums, index, length);
              	Grouping obj = dict.get(0);
                nums = obj.arr;
                index = -2;
            }
            else
            {
                prev = nums[index];
                index -= 1;
            }
        }
        
        if(index != -2)
        {
            Arrays.sort(nums);
        }
        return nums;
    }
    
    public Map<Integer, Grouping> compute(int[] nums, int index, int length)
    {
        Grouping ret = new Grouping();
        int jndex = length - 1;
        while(nums[jndex] <= nums[index])
        {
            jndex -= 1;
        }

        nums[index] += nums[jndex]; 
        nums[jndex] = nums[index] - nums[jndex]; 
        nums[index] -= nums[jndex];
        
        int[] temp = Arrays.copyOfRange(nums, index + 1, length);
        Arrays.sort(temp);
        for(int i = 0; i < temp.length; i++)
        {
            index += 1;
            nums[index] = temp[i];    
        }
        
        ret.val = jndex;
        ret.arr = nums;
      
	    Map<Integer, Grouping> hash = new HashMap<Integer, Grouping>();
      	hash.put(0, ret);
        return hash;
    }
}

class Grouping
{
    int val;
    int[] arr;
}
