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
		
		String[] NK = br.readLine().split(" ");
		int n = Integer.parseInt(NK[0]);
		int k = Integer.parseInt(NK[1]);
		
		int[] slide_arr = new int[n];
		
		for (int i = 0; i < n; i++) {
			String name = br.readLine();
			slide_arr[i] = name.length();
		}
		
		long[] length_arr = new long[21];
		Queue<Long> q = new LinkedList<Long>();
		int q_max_size = k + 1;
		
		long[] duplicated = new long[q_max_size];
		int temp_index = 0;
		
		for (int i = 0; i < q_max_size; i++) {
			if (i >= slide_arr.length)
				break;
			q.add((long) slide_arr[i]);
			if (length_arr[slide_arr[i]] == 1) {
				duplicated[temp_index] = slide_arr[i];
				temp_index += 1;
			}
			length_arr[slide_arr[i]] += 1;
		}
		
		long res = 0;
		
		for (int i = 0; i < duplicated.length; i++) {
			res += (length_arr[(int) duplicated[i]] * (length_arr[(int) duplicated[i]] - 1)) / 2;
		}
		
		for (int i = q_max_size; i < slide_arr.length; i++) {
			long removed = q.poll();
			long newone = slide_arr[i];
			length_arr[(int) removed] -= 1;
			res += length_arr[(int) newone];
			length_arr[(int) newone] += 1;
			q.add(newone);
		}
		
		bw.write(res + "");
		bw.flush();
		bw.close();

	}

}