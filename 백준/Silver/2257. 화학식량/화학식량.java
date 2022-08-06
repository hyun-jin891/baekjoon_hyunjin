import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.io.IOException;


public class Main {
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws java.io.IOException {
		String s = bf.readLine();
		
		Stack<String> stack = new Stack<String>();
		int MW = 0;
		
		for (int i = 0; i < s.length(); i++) {
			String cs = s.charAt(i) + "";
			if (cs.equals("(")) {
				stack.push(cs);
				continue;
			}
			else if (cs.equals(")")){
				int num = 0;
				while (true) {
					if (stack.peek().equals("(")) {
						stack.pop();
						stack.push(Integer.toString(num));
						break;
					}
					else {
						num += Integer.parseInt(stack.pop());
					}
				}
			}
			else if (cs.equals("H"))
				stack.push("1");
			else if (cs.equals("C"))
				stack.push("12");
			else if (cs.equals("O"))
				stack.push("16");
			else {
				int n = Integer.parseInt(stack.pop());
				stack.push(Integer.toString(n * Integer.parseInt(cs)));
			}
		}
		
		
		while (!stack.isEmpty()) {
			MW += Integer.parseInt(stack.pop());
		}
		
		bw.write(MW + "\n");
		

		bw.flush();
		bw.close();
		

	}
	
	
	
	


}