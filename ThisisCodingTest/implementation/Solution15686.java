package implementation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution15686 {
    public static int answer = Integer.MAX_VALUE;
    public static List<List<Integer>> house;
    public static List<List<Integer>> chicken;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        house = new ArrayList<>();
        chicken = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                String tk = st.nextToken();
                if (tk.equals("1"))
                    house.add(List.of(j, i));
                else if (tk.equals("2"))
                    chicken.add(List.of(j, i));
            }
        }

        System.out.println(Solution(m));
    }

    public static int Solution(int m) {
        boolean[] visit = new boolean[chicken.size()];
        getMaxFranchise(visit, 0, chicken.size(), m);
        return answer;
    }

    public static void getMaxFranchise(boolean[] visit, int point, int n, int r) {
        if (r == 0) {
            int sum = 0;
            for (List<Integer> houseloc : house) {
                int min = Integer.MAX_VALUE;
                for (int i = 0; i < visit.length; i++) {
                    if (visit[i] == false)
                        continue;
                    min = Math.min(
                            Math.abs(houseloc.get(0) - chicken.get(i).get(0))
                                    + Math.abs(houseloc.get(1) - chicken.get(i).get(1)),
                            min);
                }
                sum+=min;
            }

            answer = Math.min(sum, answer);
            return;
        }

        if (point == n)
            return;

        visit[point] = true;
        getMaxFranchise(visit, point + 1, n, r - 1);

        visit[point] = false;
        getMaxFranchise(visit, point + 1, n, r);
    }

}
