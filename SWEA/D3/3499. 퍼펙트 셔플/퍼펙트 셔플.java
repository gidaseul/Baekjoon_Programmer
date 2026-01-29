import java.io.*;
import java.util.*;

public class Solution {

	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;
	
	public static void main(String[] args) throws IOException {		
		br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine().trim();
		
		int testCase = Integer.parseInt(input);
		
		for (int i =1; i<=testCase; i++) {
			input = br.readLine().trim();
			int numberSize = Integer.parseInt(input);
			String[] array = new String[numberSize];
			st = new StringTokenizer(br.readLine().trim());
			for (int j=0; j<numberSize; j++) {
				array[j] = st.nextToken();
			}
			int range = (numberSize+1) /2; // 홀수일 경우를 대비해서 
			sb = new StringBuilder();
			sb.append("#").append(i);
			
			for(int j=0;j<range;j++) {
				sb.append(" ").append(array[j]);
				if (j+range < numberSize) {
					sb.append(" ").append(array[j+range]);
				}
				
			}

			System.out.println(sb.toString());
			}
		}
	}
