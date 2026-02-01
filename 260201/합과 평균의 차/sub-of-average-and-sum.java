import java.util.*;
import java.io.*;

public class Main {

    static BufferedReader br;
    static StringBuilder sb;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();

        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int sum = a+b+c;
        int avg = sum/3;
        int sumMinusAvg= sum-avg;

        sb.append(sum).append("\n");
        sb.append(avg).append("\n");
        sb.append(sumMinusAvg);
        System.out.println(sb.toString());
    }
}
