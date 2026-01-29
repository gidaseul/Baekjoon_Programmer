import java.io.*;
import java.util.*;

/**
 * 
 * @see #main(String[])
 *  1. 총 10개의 test case를 진행한다.
 *  	
 *  
 *  2. 각 테스트 케이스마다,
 *  	2-1. 공백 구분하여 8개의 값을 입력받는다.
 *  	
 *  3. Stack을 이용하여 계산한다.
 *  	3-1. 초기 8개의 값을 Stack에 push한다.
 *  	3-2. 사이클을 통하여 반복한다.(3-2-1이 1 cycle)
 *  		3-2-1. 가장 맨 앞의 숫자-1을 하고 뒤로 넘긴다.(push->pop)
 * 				3-2-1. 을 반복하여 진행할 때,
 * 					맨 뒷자리에 0보다 작거나 같은 경우 종료된다.
 *  
 *  
 *  
 *
 */
public class Solution {

	static BufferedReader br;
	static StringTokenizer st;
	
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		br = new BufferedReader(new InputStreamReader(System.in));
		int a =0;
		int testcase = 10;
		
		for (int i=1; i<=testcase; i++) {
			
			// 2
			String testCaseNumber = br.readLine();
			st = new StringTokenizer(br.readLine());
			
			Queue<Integer> queue = new LinkedList<>();
			for (int number=0;number<8;number++) {
				queue.add(Integer.parseInt(st.nextToken()));
			}
			
			// 3
			Other: while(true) {
				for(int cycle =1; cycle<=5; cycle++) {
				int current = queue.poll();
				int nextValue = current-cycle;
				if (nextValue<=0) {
					queue.add(0);
					break Other;
					}
				queue.add(nextValue);
				}
			}
				
			System.out.print("#" + testCaseNumber + " "); 
			for(Integer num : queue) {
			System.out.print(num+" ");
			}
			System.out.println();
		}
	}
}
