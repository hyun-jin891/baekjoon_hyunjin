

import java.util.Queue;
import java.util.LinkedList;
import java.io.*;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int L = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int Ml = Integer.parseInt(st.nextToken());
		int Mk = Integer.parseInt(st.nextToken());
		int Cammo = Integer.parseInt(br.readLine());
		Queue<Integer> q = new LinkedList<Integer>();
		
		int[] total_gun = new int[L + 1];
		total_gun[0] = 0;
		
		int[] new_gun = new int[L + 1];
		new_gun[0] = 0;
		
		
		for (int i = 0; i < L; i++) {
			int zombie_life = Integer.parseInt(br.readLine());
			q.add(zombie_life);
		}
		
		boolean flag = true;
		
		for (int i = 1; i < L + 1; i++) {
			int zombie = q.poll();
			new_gun[i] = 0;
			total_gun[i] = 0;
			
			if (i < Ml) {
				int previousGun = total_gun[i - 1];
				int update_zombie = zombie - Mk * previousGun;
				if (update_zombie <= Mk) {
					new_gun[i] += 1;
					total_gun[i] = previousGun + 1;
				}
				else {
					Cammo--;
					total_gun[i] = previousGun;
				}
			}
			else {
				int previousGun = total_gun[i - 1] - new_gun[i - Ml];
				int update_zombie = zombie - Mk * previousGun;
				if (update_zombie <= Mk) {
					new_gun[i] += 1;
					total_gun[i] = previousGun + 1;
				}
				else {
					Cammo--;
					total_gun[i] = previousGun;
				}
			}
			
			if (Cammo < 0) {
				flag = false;
				break;
			}
			
		}
		
		if (flag)
			bw.write("YES");
		else
			bw.write("NO");
		
		bw.flush();
		bw.close();
		

	}
	

}