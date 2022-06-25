import java.io.BufferedReader;

import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException; 
import java.util.StringTokenizer;

public class Main {
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static long[] h, p;
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String s = bf.readLine();
		
		int n = Integer.parseInt(s);
		int[] arr = new int[n];
		
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(bf.readLine());
		}

		for (int i : arr) {
			bw.write(numPalindrome(i) + "\n");
		}
		
	

		
		bw.flush();
		bw.close();
		

	}
	
	static int numPalindrome(int n) {
		int[] dp = new int[n + 1];
		dp[0] = 0;
		
		for (int i = 1; i <= n; i++) {
			dp[i] = 1;
			for (int j = 1; j <= i/2; j++) {
				dp[i] += dp[j]; 
			}
		}
		
		return dp[n];
	}
	


}
