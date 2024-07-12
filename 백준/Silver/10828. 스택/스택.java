import java.util.Stack;
import java.util.StringTokenizer;
import java.io.*;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		ArrayList<String> res = new ArrayList<String>();
		
		int n = Integer.parseInt(st.nextToken());
		Stack<String> s = new Stack<String>();
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int count = st.countTokens();
			
			if (count == 2) {
				st.nextToken();
				s.push(st.nextToken());
			}
			else {
				String command = st.nextToken();
				if (command.equals("pop")) {
					if (s.isEmpty())
						res.add("-1");
					else {
					String string = s.pop();
					res.add(string);
					}
				}
				else if (command.equals("size")) {
					res.add(s.size() + "");
				}
				else if (command.equals("empty")) {
					if (s.isEmpty())
						res.add("1");
					else
						res.add("0");
				}
				else {
					if (s.isEmpty())
						res.add("-1");
					else {
						res.add(s.peek());
					}
				}
			}
			
		}
		
		for (int i = 0; i < res.size(); i++) {
			if (i == res.size() - 1)
				bw.write(res.get(i));
			else
				bw.write(res.get(i) + "\n");
		}
		
		
		
		bw.flush();
		bw.close();

	}

}
