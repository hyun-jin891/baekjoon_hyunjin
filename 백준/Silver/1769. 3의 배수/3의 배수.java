import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException; 

public class Main {
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static int count = 0;
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String s = bf.readLine();
		
		boolean flag = isThreeMultiple(s);
		bw.write(Integer.toString(count) + "\n");
		
		if (flag)
			bw.write("YES");
		else
			bw.write("NO");
		
		bw.flush();
		bw.close();
		

	}
	
	static boolean isThreeMultiple(String s) {
		String newS = "";
		int sum = 0;
		
		if (s.length() == 1) {
			if (Integer.parseInt(s) % 3 == 0)
				return true;
			else
				return false;
		}
		
		count++;
		for (int i = 0; i < s.length(); i++) {
			int number = Integer.parseInt("" + s.charAt(i));
			sum += number;
			
		}
		
		newS = "" + sum;
		if (sum > 0 && sum < 10) {
			if (sum % 3 == 0)
				return true;
			else
				return false;
		}
		
		
		
		if (isThreeMultiple(newS))
			return true;
		else
			return false;
		
	}

}
