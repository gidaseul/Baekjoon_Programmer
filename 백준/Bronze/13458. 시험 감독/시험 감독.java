import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] A = new int[N];

        StringTokenizer str = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(str.nextToken());
        }


        str = new StringTokenizer(br.readLine());
        int B = Integer.parseInt(str.nextToken());
        int C = Integer.parseInt(str.nextToken());

        long totalProctors = 0;

        for (int i = 0; i < N; i++) {
            totalProctors++;
            int remaining = A[i] - B;

            if (remaining > 0) {
                totalProctors += (remaining / C);
                if (remaining % C != 0) {
                    totalProctors++;
                }
            }

        }
    System.out.println(totalProctors);
    }
}