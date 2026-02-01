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

        if (a >= 3000){
            sb.append("book");
        }else if(a<3000 && a>=1000){
            sb.append("mask");
        }else{
            sb.append("no");
        }
        
        

        System.out.println(sb.toString());
    }
}
