import java.util.Stack;
import java.io.*;
import java.util.StringTokenizer;
import java.util.ArrayList;


public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int res = 0;
		Stack<String> st = new Stack<String>();
		
		String sample = br.readLine();
		
		for (int i = 0; i < sample.length(); i++) {
			char currentChar = sample.charAt(i);
			
			if (currentChar == '(') {
				st.push(currentChar + "");
			}
			else {
				if (st.peek().equals('(' + "")) {
					st.pop();
					st.push(1 + "");
				}
				else if (!st.peek().equals(')' + "")) {
					int temp = 0;
					while (true) {
						if (st.peek().equals('(' + "")) {
							st.pop();
							st.push(temp + "");
							res += (temp + 1);
							break;
						}
						else {
							temp += Integer.parseInt(st.pop());
						}
					}
				}
			}
		}
		
		bw.write(res + "");
		
		bw.flush();
		bw.close();
		

	}

}