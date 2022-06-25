import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException; 

public class Main {
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String s = bf.readLine();
		int n = Integer.parseInt(s);
		
		
		bw.write(Integer.toString((int)Math.pow(2, n)-1) + "\n");
		
		
		hanoi(n, 1, 2, 3);
		bw.flush();
		bw.close();
		

	}
	
	static void hanoi(int n, int start, int via, int destination) throws IOException {
		if (n == 1) {
			bw.write(start + " " + destination + "\n");
			return;
		}
		
		hanoi(n - 1, start, destination, via);
		

		bw.write(start + " " + destination + "\n");
		
		hanoi(n - 1, via, start, destination);
		
		
		
		
			
		
			
	}

}
