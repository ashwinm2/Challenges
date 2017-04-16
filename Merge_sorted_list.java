// Merging 2 sorted linkedlist
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null && l2 == null)
        {
            return l1;
        }
        else if(l1 == null)
        {
            return l2;
        }
        else if(l2 == null)
        {
            return l1;
        } 
        else
        {
            ListNode temp = null;
            ListNode sol = null;
            
            while(l1 != null && l2 != null)
            {
                if(l1.val < l2.val)
                {
                    if(temp == null)
                    {
                        temp = l1;
                    }
                    else
                    {
                        temp.next = l1;    
                        temp = temp.next;
                    }
                    l1 = l1.next;
                }
                else
                {
                    if(temp == null)
                    {
                        temp = l2;
                    }
                    else
                    {
                        temp.next = l2;  
                        temp = temp.next;
                    }
                    l2 = l2.next;
                }   
                if(sol == null)
                {
                    sol = temp;
                }
            }
            
            if(l1 != null)
            {
                temp.next = l1;
            }
            else if(l2 != null)
            {
                System.out.println(temp.val);
                temp.next = l2;
            }
            
            return sol;
        }
    }
}