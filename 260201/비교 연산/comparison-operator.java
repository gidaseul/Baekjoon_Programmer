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
        
        //1
        if(a>=b){
            sb.append(1).append("\n");
        }else{
            sb.append(0).append("\n");
        }
        //2
        if(a>b){
            sb.append(1).append("\n");
        }
        else{
            sb.append(0).append("\n");
        }
        //3
        if(b>=a){
            sb.append(1).append("\n");
        }else{
            sb.append(0).append("\n");
        }
        //4
        if(b>a){
            sb.append(1).append("\n");
        }
        else{
            sb.append(0).append("\n");
        }
        if(a==b){
            sb.append(1).append("\n");
        }else{
            sb.append(0).append("\n");
        }
        if(a!=b){
            sb.append(1).append("\n");
        }
        else{
            sb.append(0).append("\n");
        }

        System.out.println(sb.toString());
    }
}
