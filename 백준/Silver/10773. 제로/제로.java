import java.util.Stack;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		Stack<Integer> s = new Stack<Integer>();
		
		int k = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < k; i++) {
			int inputInteger = Integer.parseInt(br.readLine());
			
			if (inputInteger == 0)
				s.pop();
			else
				s.push(inputInteger);
		}
		
		int sum = 0;
		
		while (!s.isEmpty()) {
			sum += s.pop();
		}
		
		bw.write(sum + "");
		
		
		
		
		
		bw.flush();
		bw.close();

	}

}