import java.io.*;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Deque;


class Coordinate{
	private int x;
	public int getX() {
		return x;
	}

	public void setX(int x) {
		this.x = x;
	}

	public int getY() {
		return y;
	}

	public void setY(int y) {
		this.y = y;
	}

	private int y;
	
	public Coordinate(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	public boolean equals(Object other) {
		if (other == null)
			return false;
		if (getClass() != other.getClass())
			return false;
		else {
			Coordinate c_other = (Coordinate)other;
			
			return (x == c_other.x && y == c_other.y);
		}
	}
	
}

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		int[][] snakeWorld = new int[N + 1][N + 1];
		int K = Integer.parseInt(br.readLine());
		StringTokenizer st = null;
		
		for (int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine());
			int y = Integer.parseInt(st.nextToken());
			int x = Integer.parseInt(st.nextToken());
			
			snakeWorld[y][x] = 1;      // 사과 위치
		}
		
		Queue<Integer> times = new LinkedList<Integer>();
		Queue<String> turns = new LinkedList<String>();
		
		int L = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < L; i++) {
			st = new StringTokenizer(br.readLine());
			times.add(Integer.parseInt(st.nextToken()));
			turns.add(st.nextToken());
		}
		
		int time = 0;
		String head_direction = "r";
		Deque<Coordinate> snake = new LinkedList<Coordinate>();
		snake.addFirst(new Coordinate(1, 1));
	
		
		while (true) {
			time++;
			int head_y = snake.peekFirst().getY();
			int head_x = snake.peekFirst().getX();
			int nextHead_y = head_y;
			int nextHead_x = head_x;
			
			if (head_direction.equals("r")) {
				nextHead_x++;
			}
			else if (head_direction.equals("l")) {
				nextHead_x--;
			}
			else if (head_direction.equals("u")) {
				nextHead_y--;
			}
			else {
				nextHead_y++;
			}
			
			if (nextHead_y > N || nextHead_x > N || nextHead_y < 1 || nextHead_x < 1)
				break;
			else if (snake.contains(new Coordinate(nextHead_x, nextHead_y)))
				break;
			
			if (snakeWorld[nextHead_y][nextHead_x] == 1) {
				snake.addFirst(new Coordinate(nextHead_x, nextHead_y));
				snakeWorld[nextHead_y][nextHead_x] = 0;
			}
			else {
				snake.addFirst(new Coordinate(nextHead_x, nextHead_y));
				snake.pollLast();
			}
			
			if (!times.isEmpty() && time == times.peek()) {
				times.poll();
				String direction_command = turns.poll();
				
				if (direction_command.equals("D")) {
					if (head_direction.equals("r"))
						head_direction = "d";
					else if (head_direction.equals("l"))
						head_direction = "u";
					else if (head_direction.equals("u"))
						head_direction = "r";
					else
						head_direction = "l";
				}
				else {
					if (head_direction.equals("r"))
						head_direction = "u";
					else if (head_direction.equals("l"))
						head_direction = "d";
					else if (head_direction.equals("u"))
						head_direction = "l";
					else
						head_direction = "r";
				}
			}
			
			
		}
		
		
		bw.write(time + "");
		
		
		bw.flush();
		bw.close();

	}

}