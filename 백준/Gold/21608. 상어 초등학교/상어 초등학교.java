import java.io.*;
import java.util.*;

public class Main {

    static int N, range;
    static int[][] map;
    static int[] order;
    static int[] studentOther;
    static boolean[][] isFavorite;

    // 상하좌우 탐색
    static int[] dr = {-1,1,0,0};
    static int[] dc = {0,0,-1,1};

    // 클래스
// 후보지 칸의 정보를 담는 클래스. 정렬 규칙을 내장함.
    static class Seat implements Comparable<Seat> {
        int r, c, favCount, emptyCount;

        public Seat(int r, int c, int f, int e) {
            this.r = r; this.c = c; this.favCount = f; this.emptyCount = e;
        }

        // 문제의 우선순위 조건을 정렬 규칙으로 정의
        @Override
        public int compareTo(Seat o) {
            // 1. 좋아하는 친구가 많은 순 (내림차순)
            if (this.favCount != o.favCount) return o.favCount - this.favCount;
            // 2. 인접한 빈칸이 많은 순 (내림차순)
            if (this.emptyCount != o.emptyCount) return o.emptyCount - this.emptyCount;
            // 3. 행 번호가 작은 순 (오름차순)
            if (this.r != o.r) return this.r - o.r;
            // 4. 열 번호가 작은 순 (오름차순)
            return this.c - o.c;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        range = N * N;

        map = new int[N][N];
        order = new int[range];
        isFavorite = new boolean[range + 1][range + 1];

        for (int i = 0; i < range; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine());
            int student = Integer.parseInt(str.nextToken());
            order[i] = student;
            for (int j = 0; j < 4; j++) {
                int favorite = Integer.parseInt(str.nextToken());
                isFavorite[student][favorite] = true;
            }
        }
        // 2. 학생 순서대로 자리 배치 (Solve)
        for (int studentId : order) {
            placeStudent(studentId);
        }

        // 3. 결과 계산 및 출력 (Output)
        System.out.println(calculateSatisfaction());
    }
        // 특정 학생을 최적의 칸에 앉히는 메서드
        static void placeStudent(int studentId) {
            List<Seat> candidates = new ArrayList<>();

            // 모든 칸을 전수조사 (N x N)
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    // 이미 누가 앉아있으면 건너뜀
                    if (map[r][c] != 0) continue;

                    int fCnt = 0; // 주변 좋아하는 친구 수
                    int eCnt = 0; // 주변 빈칸 수

                    // 상하좌우 4방향 탐색
                    for (int d = 0; d < 4; d++) {
                        int nr = r + dr[d];
                        int nc = c + dc[d];

                        // 교실 범위를 벗어나지 않는지 확인
                        if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                            if (map[nr][nc] == 0) eCnt++; // 빈칸이면 eCnt 증가
                            else if (isFavorite[studentId][map[nr][nc]]) fCnt++; // 좋아하는 친구면 fCnt 증가
                        }
                    }
                    // 이 칸의 정보를 리스트에 담음
                    candidates.add(new Seat(r, c, fCnt, eCnt));
                }
            }

            // Seat 클래스에 정의한 compareTo 규칙에 따라 정렬
            Collections.sort(candidates);

            // 정렬 후 가장 앞에 있는(0번) 칸이 최적의 자리
            Seat best = candidates.get(0);
            map[best.r][best.c] = studentId; // 학생 배치!
        }

        // 모든 학생의 배치가 끝난 후 최종 만족도 합산
        static int calculateSatisfaction() {
            int totalScore = 0;

            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    int studentId = map[r][c];
                    int count = 0;

                    for (int d = 0; d < 4; d++) {
                        int nr = r + dr[d];
                        int nc = c + dc[d];

                        if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                            if (isFavorite[studentId][map[nr][nc]]) count++;
                        }
                    }

                    // 점수 합산: 0명=0, 1명=1, 2명=10, 3명=100, 4명=1000
                    if (count > 0) {
                        totalScore += (int) Math.pow(10, count - 1);
                    }
                }
        } return totalScore;
    }
}
