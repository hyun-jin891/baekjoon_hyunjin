import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.io.IOException;
import java.util.ArrayList;


public class Main {
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws java.io.IOException {
		String s = bf.readLine();
		
		Stack<String> stack = new Stack<String>();
		
		
		for (int i = 0; i < s.length(); i++) {
			String cs = s.charAt(i) + "";
			String ncs = "";
			ArrayList<String> num = new ArrayList<String>();
			
			if (cs.equals(")")){
				while (true) {
					if (stack.peek().equals("(")) {
						stack.pop();
						if (stack.isEmpty()) {
							break;
						}
						if (stack.peek().charAt(0) == '0') {
							stack.pop();
							break;
						}
						long count = Long.parseLong(stack.pop().charAt(0) + "");
						for (int k = 0; k < ncs.length(); k++) {
							stack.push(ncs.charAt(ncs.length() - k - 1) + "" + Long.parseLong(num.get(ncs.length() - k - 1)) * count);
						}
						
						break;
					}
					else {
						String element = stack.pop();
						ncs += element.charAt(0) + "";
						num.add(element.substring(1));
					}
				}
			}
			
			else if (cs.equals("(")) {
				stack.push(cs);
			}

			else {
				stack.push(cs + "1");
			}
		}
		
		long result = 0L;
		while (!stack.isEmpty()) {
			if (stack.peek().length() == 1) {
				result++;
				stack.pop();
			}
			
			else {
				result += Long.parseLong(stack.pop().substring(1));
			}
		}
		
		bw.write(result + "\n");
		

		bw.flush();
		bw.close();
		

	}
	
	
	
	


}