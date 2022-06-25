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

		StringTokenizer f = new StringTokenizer(s);
		
		int N = Integer.parseInt(f.nextToken());
		long X = Long.parseLong(f.nextToken());
		
		h = new long[N+1];
		p = new long[N+1];
		
		h[0] = 1;
		p[0] = 1;
		
		for (int i = 1; i <= N; i++) {
			h[i] = 1 + h[i-1] + 1 + h[i-1] + 1;
			p[i] = p[i-1] + 1 + p[i-1];
		}
		
		
		
		
		
		long countP = getP(N, X);
		
		
		
		bw.write(countP + "\n");

		
		bw.flush();
		bw.close();
		

	}
	
	static long getP(int level, long max) {
		if (level == 0) {
			if (max == 0)
				return 0;
			else if (max == 1)
				return 1;
		}
		
		if (max == 1)
			return 0;
		
		if (max <= 1 + h[level - 1]) {
			return getP(level - 1, max - 1);
		}
		
		else if (max == 1 + h[level - 1] + 1) {
			return 1 + p[level - 1];
		}
		
		else if (max <= 1 + h[level - 1] + 1 + h[level - 1]) {
			return getP(level - 1, max - (1 + h[level - 1] + 1)) + p[level - 1] + 1;
		}
		
		else {
			return p[level - 1] + 1 + p[level - 1];
		}
		
		
		
		
		
		
	}

}
