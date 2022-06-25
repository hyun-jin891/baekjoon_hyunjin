import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException; 
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		String s = bf.readLine();
		int n = Integer.parseInt(s);
		
		for (int i = 0; i < n; i++) {
			String line = bf.readLine();
			int sum = 0;
			StringTokenizer f = new StringTokenizer(line);
			
			while (f.hasMoreTokens()) {
				sum += Integer.parseInt(f.nextToken());
			}
			bw.write(sum + "\n");
		}
		

		
		bw.flush();
		bw.close();
		

	}
	
	
	
	


}