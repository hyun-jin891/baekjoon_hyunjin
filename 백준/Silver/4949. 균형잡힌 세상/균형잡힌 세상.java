import java.util.Stack;
import java.io.*;
import java.util.StringTokenizer;
import java.util.ArrayList;


public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		ArrayList<String> res = new ArrayList<String>();
		
		while (true) {
			String currentS = br.readLine();
			if (currentS.equals(".")) {
				break;
			}
			Stack<Character> st = new Stack<Character>();
			boolean resFlag = true;
			
			for (int i = 0; i < currentS.length(); i++) {
				char currentChar = currentS.charAt(i);
				if (currentChar == '[' || currentChar == '(') {
					st.push(currentChar);
				}
				else if (currentChar == ']') {
					if (st.isEmpty()) {
						res.add("no");
						resFlag = false;
						break;
					}
					if (st.peek() != '[') {
						res.add("no");
						resFlag = false;
						break;
					}
					else {
						st.pop();
						continue;
					}
				}
				else if (currentChar == ')') {
					if (st.isEmpty()) {
						res.add("no");
						resFlag = false;
						break;
					}
					if (st.peek() != '(') {
						res.add("no");
						resFlag = false;
						break;
					}
					else {
						st.pop();
						continue;
					}
				}
			}
			if (resFlag && st.isEmpty()) {
				res.add("yes");
			}
			if (resFlag && !st.isEmpty()) {
				res.add("no");
			}
			
			
		}

		
		for (int i = 0; i < res.size(); i++) {
			bw.write(res.get(i)+"\n");
			
		}
		
		bw.flush();
		bw.close();
		

	}

}