import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException; 

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String s = bf.readLine();
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)); 
		bw.write(isAkaraka(s));
		bw.flush();
		bw.close();

	}
	
	static boolean isPalindrome(String s) {
		boolean flag = false;
		int index = 0;
		while (true) {
			if (s.charAt(index) != s.charAt(s.length() - index -1))
				break;
			if (index == (s.length() - 1) / 2) {
				flag = true;
				break;
			}
			index++;
		}
		if (!flag)
			return false;
		else
			return true;
	}
	
	static String isAkaraka(String s) {
		if (!isPalindrome(s))
			return "IPSELENTI";
		if (s.length() == 1)
			return "AKARAKA";
		int length = s.length() / 2;
		
		if (isAkaraka(s.substring(0, length)).equals("AKARAKA") && isAkaraka(s.substring(s.length() - length, s.length())).equals("AKARAKA"))
			return "AKARAKA";
		
		return "IPSELENTI";
		
	}

}
