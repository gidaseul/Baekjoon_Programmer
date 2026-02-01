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

        if(a<b){
            sb.append(1);
        }else{
            sb.append(0);
        }
        sb.append(" ");
        if(a==b){
            sb.append(1);
        }
        else{
            sb.append(0);
        }

        System.out.println(sb.toString());
    }
}
