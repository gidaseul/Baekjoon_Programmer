import java.util.*;
import java.io.*;

public class Main {

    static BufferedReader br;
    static StringBuilder sb;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));

        // 1줄 짜리 공백 없이 읽을 때(통째로 읽기)
        int T = Integer.parseInt(br.readLine().trim());
        for (int i = 0; i < T; i++) {
            boolean isValid = true;
            sb = new StringBuilder();
            String line = br.readLine().trim();
            Stack<Character> s = new Stack<>();
            char[] arr = line.toCharArray(); // 이렇게 해서 입력 배열처럼 가지기
            for (char c : arr) {
                if (c == '(') {
                    s.push(c);
                } else {
                    if (s.empty()) {
                        isValid = false;
                        break;
                    }
                    s.pop();
                }
            }
            if (isValid && s.isEmpty()) {
                sb.append("YES");
            } else {
                sb.append("NO");
            }
            System.out.println(sb.toString());
        }
    }
}
