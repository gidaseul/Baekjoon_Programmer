import java.io.*;
import java.util.*;
import java.math.BigInteger; 

public class Solution {

	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;
	
	public static void main(String[] args) throws IOException {		
		br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine().trim();
		
		int testCase = Integer.parseInt(input);
		
		for (int i =1; i<=testCase; i++) {

			st = new StringTokenizer(br.readLine().trim());
			sb = new StringBuilder();
			
			// 양의 정수이기 때문에 -> BigInteger를 사용해도 무방함.
			
			// 소수점까지 동일해야 한다면 BigDecimal을 사용하는 것이 좋음.
			
			BigInteger a = new BigInteger(st.nextToken());
			BigInteger b = new BigInteger(st.nextToken());
			
			BigInteger result = a.add(b);
			sb.append("#").append(i).append(" ").append(result);
			System.out.println(sb.toString());
			}
		}
	}