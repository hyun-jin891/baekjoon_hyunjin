
import java.io.*;



public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		int[] inorderArr = new int[n];
		String[] inStr = br.readLine().split(" ");
		for (int i = 0; i < inStr.length; i++) {
			inorderArr[i] = Integer.parseInt(inStr[i]);
		}
		int[] postorderArr = new int[n];
		String[] postStr = br.readLine().split(" ");
		for (int i = 0; i < postStr.length; i++) {
			postorderArr[i] = Integer.parseInt(postStr[i]);
		}
		
		Node root = new Node(postorderArr[n-1]);
		
		Tree tree = new Tree(root);
		
		createTree(inorderArr, 0, n - 1, postorderArr, 0, n - 1, root);
		
		tree.preOrder(root, bw);

		bw.flush();
		bw.close();
		

	}
	
	public static void createTree(int[] inorderArr, int inStart, int inEnd, int[] postorderArr, int postStart, int postEnd, Node p) {
		if (inStart >= inEnd)
			return;
		if (postStart >= postEnd)
			return;
		if (p == null)
			return;
		int newinLeftStart = 0;
		int newinLeftEnd = 0;
		int newinRightStart = 0;
		int newinRightEnd = 0;
		
		for (int i = inStart; i < inEnd + 1; i++) {
			if (inorderArr[i] == p.data) {
				newinLeftStart = inStart;
				newinLeftEnd = i - 1;
				break;
			}
		}
		newinRightStart = newinLeftEnd + 2;
		newinRightEnd = inEnd;
		
		int newpostLeftStart = postStart;
		int newpostLeftEnd = postStart + (newinLeftEnd - newinLeftStart);
		int newpostRightStart = newpostLeftEnd + 1;
		int newpostRightEnd = postEnd - 1;
		
		
		Node leftNode = null;
		Node rightNode = null;
		
		if (newinLeftStart <= newinLeftEnd) {
			leftNode = new Node(postorderArr[newpostLeftEnd]);
		}
		
		if (newinRightStart <= newinRightEnd) {
			rightNode = new Node(postorderArr[newpostRightEnd]);
		}
			
		p.setLeft(leftNode);
		p.setRight(rightNode);
		
		createTree(inorderArr, newinLeftStart, newinLeftEnd, postorderArr, newpostLeftStart, newpostLeftEnd, leftNode);
		createTree(inorderArr, newinRightStart, newinRightEnd, postorderArr, newpostRightStart, newpostRightEnd, rightNode);
		
		
	}

}

class Node{
	int data;
	Node left;
	Node right;
	
	Node(int data){
		this.data = data;
		left = null;
		right = null;
	}
	
	void setLeft(Node left) {
		this.left = left;
	}
	
	void setRight(Node right) {
		this.right = right;
	}
}

class Tree{
	Node root;
	
	Tree(Node root){
		this.root = root;
	}
	
	void preOrder(Node parent, BufferedWriter bw) throws NumberFormatException, IOException {

		if (parent == null)
			return;
		
		bw.write(parent.data + " ");
		preOrder(parent.left, bw);
		preOrder(parent.right, bw);
	}
}