import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException; 
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static ArrayList<Long> dp;
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		String s = bf.readLine();
		int n = Integer.parseInt(s);
		
		dp = new ArrayList<Long>();
		dp.add(3L);
		
		
		int count = 1;
		
		while (true) {
			dp.add(count, dp.get(count-1) * 2 + count + 2 + 1);
			
			if (dp.get(count) >= n)
				break;
			count++;
		}
		
		bw.write(search(n));

		
		bw.flush();
		bw.close();
		

	}
	
	static char search(long n) {
		int k = 0;
		for (int i = 0; dp.get(i) < n; i++) {
			k = i;
		}
		k++;
		
		if (n <= 3L) {
			if (n == 1L)
				return 'm';
			else
				return 'o';
		}
		
		if (n <= dp.get(k - 1)) {
			return search(n);
		}
		
		else if (n <= dp.get(k - 1) + 1 + k + 2) {
			long index = n - dp.get(k - 1);
			if (index == 1L)
				return 'm';
			else
				return 'o';
		}
		
		else {
			return search(n - dp.get(k - 1) - (k + 3));
		}
		
		
		
		
	}
	
	


}
