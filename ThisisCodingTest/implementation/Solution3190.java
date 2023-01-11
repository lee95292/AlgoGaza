/*
백준 3190 뱀
 */
package implementation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution3190 {
    static int n;
    static int k;
    static int l;
    static int[] dx = { 1, 0, -1, 0 };
    static int[] dy = { 0, 1, 0, -1 };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());
        int[][] apples = new int[k][2];
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            apples[i][1] = Integer.parseInt(st.nextToken()) - 1;
            apples[i][0] = Integer.parseInt(st.nextToken()) - 1;

        }

        l = Integer.parseInt(br.readLine());
        int[][] directions = new int[l][2]; // time, direction. L:-1 , D: 1
        for (int i = 0; i < l; i++) {
            st = new StringTokenizer(br.readLine());

            directions[i][0] = Integer.parseInt(st.nextToken());
            String dir = st.nextToken();
            if (dir.equals("L"))
                directions[i][1] = -1;
            else if (dir.equals("D"))
                directions[i][1] = 1;
        }
        System.out.println(Solution(apples, directions));
    }

    public static int Solution(int[][] apples, int[][] directions) {
        int[][] map = new int[n][n];
        for (int i = 0; i < k; i++) {
            map[apples[i][1]][apples[i][0]] = 2;
        }
        int[] location = { 0, 0 };
        int direction = 0;
        int didx = 0;
        map[0][0] = 1;
        Queue<List<Integer>> snake = new LinkedList<>();
        snake.add(List.of(0, 0));
        for (int i = 1; i <= 10000; i++) {
            location[0] += dx[direction];
            location[1] += dy[direction];

            // 범위체크
            if (location[0] < 0 || location[1] < 0 || location[0] >= n || location[1] >= n)
                return i;

            // 충돌체크
            if (map[location[1]][location[0]] == 1)
                return i;
            // 꼬리삭제
            if (map[location[1]][location[0]] != 2) {
                List<Integer> tail = snake.poll();
                map[tail.get(1)][tail.get(0)] = 0;
            }

            snake.add(List.of(location[0], location[1]));
            map[location[1]][location[0]] = 1;
            // 방향전환
            if (didx < directions.length && i == directions[didx][0]) {
                direction += directions[didx][1];
                if (direction == 4)
                    direction = 0;
                else if (direction == -1)
                    direction = 3;
                didx++;
            }
        }
        return 0;
    }

}