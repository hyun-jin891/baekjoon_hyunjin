import java.util.Stack;
import java.io.*;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		String seq = "";
		Stack<Integer> s = new Stack<Integer>();
		Stack<Integer> numList = new Stack<Integer>();
		ArrayList<Character> res = new ArrayList<Character>();
		StringBuilder sb = new StringBuilder();
		
		for (int i = 0; i < n; i++) {
			numList.push((n - i));
		}

		boolean flag = false;
		
		for (int i = 0; i < n; i++) {
			int currentNum = Integer.parseInt(br.readLine());
			
			if (s.contains(currentNum)) {
				while (!s.peek().equals(currentNum)) {
					s.pop();
					res.add('-');
				}
				s.pop();
				res.add('-');
				
			}
			
			else if (numList.contains(currentNum)) {
				while (!numList.peek().equals(currentNum)) {
					s.push(numList.pop());
					res.add('+');
				}
				numList.pop();
				res.add('+');
				res.add('-');
			}
			
			else {
				flag = true;
				break;
			}
			
		}
		
		if (flag)
			bw.write("NO");
		else {
			for (int i = 0; i < res.size(); i++) {
				if (i == res.size() - 1)
					bw.write(res.get(i));
				else
					bw.write(res.get(i) + "\n");
			}
		}
		
		

		
		
		bw.flush();
		bw.close();

	}

}