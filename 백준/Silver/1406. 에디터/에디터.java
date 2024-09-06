import java.util.Stack;
import java.io.*;
import java.util.StringTokenizer;
import java.util.ArrayList;


public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String currentStr = br.readLine();
		int n = Integer.parseInt(br.readLine());
		Stack<String> left_st = new Stack<String>();
		Stack<String> right_st = new Stack<String>();
		
		for (int i = 0; i < currentStr.length(); i++) {
			left_st.push(currentStr.charAt(i) + "");
		}
		
		for (int i = 0; i < n; i++) {
			String[] temp = br.readLine().split(" ");
			String command = temp[0];
			
			String obj = "";
			
			if (temp.length != 1) {
				obj = temp[1];
			}
				 
			if (command.equals("P")) {
				left_st.push(obj);
			}
			else if (command.equals("L")) {
				if (!left_st.isEmpty())
					right_st.push(left_st.pop());
			}
			else if (command.equals("D")) {
				if (!right_st.isEmpty())
					left_st.push(right_st.pop());
			}
			else {
				if (!left_st.isEmpty())
					left_st.pop();
			}
			
		}
		
		Object[] left_arr = left_st.toArray();
		
		for (int i = 0; i < left_arr.length; i++) {
			bw.write(left_arr[i] + "");
			
		}
		
		while (!right_st.isEmpty()) {
			bw.write(right_st.pop());
		}
		
		bw.flush();
		bw.close();

	}

}