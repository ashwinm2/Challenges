# Directed Acyclic Graph
package cincaphi;

import java.util.*;

/**
 *
 * @author Ashwin Murthy
 */
class Node
{
    String name;
    List<Node> children = new ArrayList<Node>();
    
    public Node(String name, Node child)
    {
        this.name = name;
        if(child != null)
        {
            this.children.add(child);
        }
    }
}

public class Graph {
    Map<String, Node> nodes = new HashMap<String, Node>();
    
    public boolean checkConn(Node start, Node end)
    {
        List<Node> track = new ArrayList<Node>();
        Map<String, Integer> lookup = new HashMap<String, Integer>();
        track.add(start);
        int index = 0;
        String source = end.name;
        while(index < track.size())
        {
            Node temp = track.get(index);
            List<Node> tempchild = temp.children;
            int length = tempchild.size();
            for(int jndex = 0; jndex < length; jndex++)
            {
                String child = tempchild.get(jndex).name;
                if(source.equals(child))
                {
                    return false;
                }
                else
                {
                    if(lookup.get(child) == null)
                    {
                        track.add(tempchild.get(jndex));
                        lookup.put(child, jndex);
                    }
                }
            }
            index += 1;
        }
        return true;
    }
    
    
    public boolean exist(Node source, String destination)
    {
        List<Node> temp = source.children;
        int length = temp.size();
        for(int index = 0; index < length; index++)
        {
            if(temp.get(index).name.equals(destination))
            {
                return true;
            }
        }
        return false;
    }
            
    public boolean addEdge(String source, String destination){
        if(nodes.get(source) == null && nodes.get(destination) == null)
        {
            Node dest = new Node(destination, null);
            Node snew = new Node(source, dest);
            nodes.put(source, snew);
            nodes.put(destination, dest);
            
        }
        else if(nodes.get(source) == null)
        {
            Node dest = nodes.get(destination);
            Node snew = new Node(source, dest);
            nodes.put(source, snew);
        }
        else if(nodes.get(destination) == null)
        {
            Node dest = new Node(destination, null);
            Node snew = nodes.get(source);
            snew.children.add(dest);
            nodes.put(source, snew);
            nodes.put(destination, dest);
        }
        else
        {
            Node dest = nodes.get(destination);
            Node snew = nodes.get(source);
            if(exist(snew, destination))
            {
                System.out.println("The edge already exists");
            }
            else
            {
                if(checkConn(dest, snew))
                {
                    snew.children.add(dest);
                }
                else
                {
                    return false;
                }
            }
        }
        return true;
    }
    
    public void print()
    {
        for(String key: nodes.keySet())
        {
            List<Node> temp = nodes.get(key).children;
            int length = temp.size();
            System.out.print(key + " - ");
            for(int index = 0; index < length; index++)
            {
                Node n = temp.get(index);
                System.out.print(n.name + " ");
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        Graph obj = new Graph();
        obj.addEdge("a", "b");
        obj.addEdge("b", "c");
        obj.addEdge("b", "d");
        obj.addEdge("d", "c");
        System.out.println(obj.addEdge("d", "c"));
        obj.print();
    }
}
