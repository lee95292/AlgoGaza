package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class J1991 {
    public static class Node {
        String name;
        Node ch2;
        Node ch1;

        Node(String name) {
            this.name = name;
            tree.put(name, this);
        }
    }

    static Map<String, Node> tree;
    static Node root;
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        tree = new HashMap<>(n);
        for (int i = 0; i < n; i++) {
            String[] x = br.readLine().split(" ");
            Node curnode;
            if (tree.get(x[0]) == null)
                curnode = new Node(x[0]);
            else
                curnode = tree.get(x[0]);
            if (x[0].equals("A"))
                root = curnode;
            if (!x[1].equals(".")) {
                curnode.ch1 = new Node(x[1]);
            }
            if (!x[2].equals("."))
                curnode.ch2 = new Node(x[2]);
        }
        traverse(root, 0);
        System.out.println();
        traverse(root, 1);
        System.out.println();
        traverse(root, 2);
    }

    public static void traverse(Node node, int v) {

        if (v == 0)
            System.out.print(node.name);
        if (node.ch1 != null)
            traverse(node.ch1, v);
        if (v == 1)
            System.out.print(node.name);
        if (node.ch2 != null)
            traverse(node.ch2, v);
        if (v == 2)
            System.out.print(node.name);
    }

}
