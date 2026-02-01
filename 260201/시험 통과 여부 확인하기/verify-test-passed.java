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
        

        if(a >= 80){
            sb.append("pass");
        }else{
            int x =80-a;
            sb.append(x).append(" more score");
        }
        

        System.out.println(sb.toString());
    }
}
