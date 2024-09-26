import java.io.*;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		
		int N = Integer.parseInt(br.readLine());
		int[] starts = new int[N];
		int[] ends = new int[N];
		
		for (int i = 0; i < N; i++) {
			String[] classInfo = br.readLine().split(" ");
			starts[i] = Integer.parseInt(classInfo[0]);
			ends[i] = Integer.parseInt(classInfo[1]);
		}
		
		minheap pqStarts = new minheap(N+1, starts);
		minheap pqEnds = new minheap(N+1, ends);
		
		for (int i = 0; i < N; i++) {
			pqStarts.addHeap(i);
			pqEnds.addHeap(i);
		}
		

		
		
		int numClass = 0;
		
		int curMinEndIndex = pqEnds.deleteHeap();
		int curMinEnd = ends[curMinEndIndex];
		
		if (pqEnds.realSize == 1 || pqEnds.realSize == 0)
			numClass++;
		else {
			for (int i = 0; i < N; i++) {

				int curClassStartIndex = pqStarts.deleteHeap();

				
				int curClassStart = starts[curClassStartIndex];


				
				if ((curClassStart < curMinEnd) || (curClassStart == curMinEnd && curMinEndIndex == curClassStartIndex && starts[curClassStartIndex] == ends[curClassStartIndex])) {

					numClass++;
				}
				else {
					curMinEndIndex = pqEnds.deleteHeap();
					
					curMinEnd = ends[curMinEndIndex];
					
			}
		}
		
	
		

	}
		bw.write(numClass + "");
		
		bw.flush();
		bw.close();
	

}
}

class minheap{
	int realSize;
	int[] heapArr;
	int[] stORend;
	int Capacity;
	
	minheap(int Capacity, int[] arr){
		realSize = 1;
		heapArr = new int[Capacity];
		heapArr[0] = -1;
		this.Capacity = Capacity;
		stORend = arr;
	}
	
	int checkSpace() {
		return Capacity - realSize;
	}
	
	void addHeap(int data) {
		int pos = realSize;
		heapArr[pos] = data;
		realSize++;
		
		while (pos > 1 && stORend[heapArr[pos]] < stORend[heapArr[pos/2]]) {
			int temp = heapArr[pos];
			
			heapArr[pos] = heapArr[pos/2];
			heapArr[pos/2] = temp;
			
			pos = pos/2;
		}
	}
	
	int deleteHeap() {
		if (realSize <= 1)
			return -1;
		int pos = 1;
		int res = heapArr[pos];
		heapArr[pos] = heapArr[realSize - 1];
		heapArr[realSize - 1] = -1;
		realSize--;
		
		while (pos * 2 < realSize) {
			int nextMinIndex = pos;
			
			if (stORend[heapArr[pos]] > stORend[heapArr[pos * 2]])
				nextMinIndex = pos * 2;
			
			if (pos * 2 + 1 < realSize && stORend[heapArr[pos]] > stORend[heapArr[pos * 2 + 1]]) {
				if (stORend[heapArr[pos * 2 + 1]] < stORend[heapArr[pos * 2]])
					nextMinIndex = pos * 2 + 1;
			}
			
			if (nextMinIndex == pos)
				break;
			
			int temp = heapArr[pos];
			heapArr[pos] = heapArr[nextMinIndex];
			heapArr[nextMinIndex] = temp;
			
			pos = nextMinIndex;
			
			
		}
		return res;
	}
	
	void printHeap() {
		for (int i = 1; i < realSize; i++) {
			System.out.println(stORend[heapArr[i]]);
		}
	}
	
}

