
import java.util.Stack;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.io.*;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		ArrayList<String> inputString = new ArrayList<String>();
		
		int n = Integer.parseInt(st.nextToken());
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			inputString.add(st.nextToken());
		}
		
		ArrayList<String> res = new ArrayList<String>();
		
		for (int i = 0; i < inputString.size(); i++) {
			Stack<Character> s = new Stack<Character>();
			String currentP = inputString.get(i);
			boolean flag = false;
			for (int j = 0; j < currentP.length(); j++) {
				char currentC = currentP.charAt(j);
				if (currentC == '(')
					s.push(currentC);
				else {
					if (s.isEmpty()) {
						res.add("NO");
						flag = true;
						break;
					}
					else {
						s.pop();
					}
				}
			}
			if (flag)
				continue;
			if (s.isEmpty())
				res.add("YES");
			else
				res.add("NO");
			
		}
		
		
		
		for (int i = 0; i < res.size(); i++) {
			bw.write(res.get(i) + "\n");
		}
		
		
		
		bw.flush();
		bw.close();
		

	}

}