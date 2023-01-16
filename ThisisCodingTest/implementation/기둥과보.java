package implementation;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    static int[][] map;

    public static void main(String[] args) throws IOException {
        int n = 5;
        // int[][] build_frame = { { 0, 0, 0, 1 }, { 2, 0, 0, 1 }, { 4, 0, 0, 1 }, { 0, 1, 1, 1 }, { 1, 1, 1, 1 },
        //         { 2, 1, 1, 1 }, { 3, 1, 1, 1 }, { 2, 0, 0, 0 }, { 1, 1, 1, 0 }, { 2, 2, 0, 1 } };

        int[][] build_frame ={{1,0,0,1},{1,1,1,1},{2,1,0,1},{2,2,1,1},{5,0,0,1},{5,1,0,1},{4,2,1,1},{3,2,1,1}};
        System.out.println(Arrays.toString(solution(n, build_frame)));
        for (int[] a : map) {
            System.out.println(Arrays.toString(a));
        }
    }

    public static int[][] solution(int n, int[][] build_frame) {
        n+=1;
        map = new int[n + 1][n + 1];

        for (int i = 0; i < build_frame.length; i++) {
            int x = build_frame[i][0];
            int y = build_frame[i][1];
            int a = build_frame[i][2]; // 0 : 기둥, 1:보
            int b = build_frame[i][3]; // 0: 삭제, 1: 설치

            if (b == 0 && canRemove(x, y, a,n)) {
                if (a == 0)
                    map[y][x] -= 1;
                else
                    map[y][x] -= 2;
            } else if (b == 1 && canBuild(x, y, a,n)) {
                if (a == 0)
                    map[y][x] += 1;
                else
                    map[y][x] += 2;
            }
            // for (int[] r : map) {
            //     System.out.println(Arrays.toString(r));
            // }
        }
        List<int[]> ans = new ArrayList<>();
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(map[j][i] == 1) ans.add([i,j,0]);
                else if(map[j][i] == 2)ans.add(List.of(i,j,1));
                    
                else if(map[j][j] == 3){
                    ans.add(List.of(i,j,0));
                    ans.add(List.of(i,j,1));
                }
                
            }
        }
        int[][] answer = new int[ans.size()][3];
        for(int i=0 ;i<ans.size(); i++){
            answer[i][0] = ans.get(i).get(0);
            answer[i][1] = ans.get(i).get(1);
            answer[i][2] = ans.get(i).get(2);
        }
        return answer;
    }

    public static boolean canBuild(int x, int y, int a, int n) {
        if (a == 0) { // 기둥
            if (y == 0)
                return true;
            if ((x > 0 && map[y][x - 1] >= 2) // 왼쪽에 보
                    || (x + 1 < n && map[y][x + 1] >= 2) // 오른쪽에 보
                    || (y > 0 && map[y - 1][x] % 2 == 1))// 밑에 기둥
                return true;
        }

        if (a == 1) {// 보
            if ((x > 1 && x + 1 < n && map[y][x - 1] >= 2 && map[y][x - 1] >= 2)// 양옆 보
                    || (y > 0 && map[y - 1][x] % 2 == 1) // 왼쪽 기둥
                    || (y > 0 && x + 1 < n && map[y - 1][x + 1] % 2 == 1)) // 오른쪽 기둥
                return true;
        }
        return false;
    }

    public static boolean canRemove(int x, int y, int a,int n) {
        boolean flag = true;

        if (a == 0) { // 기둥
            map[y][x] -= 1;

            if (y > 0 && map[y - 1][x] % 2 == 1) {
                map[y - 1][x] -= 1;
                if (!canBuild(x, y - 1, 1,n))
                    flag = false;
                map[y - 1][x] += 1;
            }
            if (flag && x > 0 && map[y][x - 1] >= 2) {      
                map[y][x - 1] -= 2;
                if (!canBuild(x - 1, y, 2,n))
                    flag = false;
                map[y][x - 1] += 2;
            }
            if (flag && x + 1 < n && map[y][x + 1] >= 2) {
                map[y][x + 1] -= 2;
                if (!canBuild(x + 1, y, 2,n))
                    flag = false;
                map[y][x + 1] += 2;
            }
            map[y][x] += 1;
        } else { // 보
            map[y][x] -= 2;

            if (x > 0 && map[y][x - 1] >= 2) {
                map[y][x - 1] -= 2;
                if (!canBuild(x - 1, y, 2,n))
                    flag = false;
                map[y][x - 1] += 2;
            }

            if (flag && x + 1 < n && map[y][x + 1] >= 2) {
                map[y][x + 1] -= 2;
                if (!canBuild(x + 1, y, 2,n))
                    flag = false;
                map[y][x + 1] += 2;
            }

            if (flag && x + 1 < n && map[y][x + 1] % 2 == 1) {
                map[y][x + 1] -= 1;
                if (!canBuild(x + 1, y, 1,n))
                    flag = false;
                map[y][x + 1] += 1;
            }

            if (flag && map[y][x] % 2 == 1) {
                map[y][x] -= 1;
                if (!canBuild(x, y, 1,n))
                    flag = false;
                map[y][x] += 1;
            }
            map[y][x] += 2;
        }
        return flag;
    }
}