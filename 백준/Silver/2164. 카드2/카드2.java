import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.io.*;
import java.util.StringTokenizer;
import java.util.ArrayList;


public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		Queue<Integer> q = new LinkedList<Integer>();
		
		for (int i = 1; i < n + 1; i++) {
			q.add(i);
		}
		
		boolean flag = false;
		
		while (q.size() != 1) {
			q.poll();
			int restart = q.poll();
			q.add(restart);
		}
		
		bw.write(q.poll() + "");
		bw.flush();
		bw.close();

	}

}