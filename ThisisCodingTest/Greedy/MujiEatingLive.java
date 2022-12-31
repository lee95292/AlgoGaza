

/*
무지의 먹방 라이브 https://school.programmers.co.kr/learn/courses/30/lessons/42891
Solution.
1) food_times 정렬 후, 순회하면서 i번째 음식을 먹는 시간과 i 이후 원소 개수를 곱하면서 네트워크 오류시점인 K를 최대한 줄여나간다.

2) K를 최대한으로 줄였을 때, 무지가 먹은 음식의 소요시간 limit를 기반으로, K 시점에 몇번째 음식을 먹었는지 체크한다.

Checkpoint
1.  효율성2번 틀리는 문제
cre * met <= k 부분: cre, met각각은 int 범위 내에 있지만, 둘을 곱하면 int범위를 초과. 따라서 아래와 같이 수정!
(long)cre*met <= k

2. 풀고나서 다른 풀이를 보니까 PQ로 푼경우가 있는듯. 풀이 확인해보기
*/

package Greedy;

import java.util.Arrays;

public class MujiEatingLive {
    public static void main(String[] args) {
        System.out.println(Solution(new int[] { 3, 1, 2 }, 5));
        System.out.println(Solution(new int[] { 4, 1, 2, 8, 7, 3, 6 }, 15));
        System.out.println(Solution(new int[] { 100, 3, 1, 1, 1 }, 5));
        System.out.println(Solution(new int[] { 1, 3, 103, 100, 1 }, 102));
        System.out.println(Solution(new int[] { 100, 100,101 }, 300));
    }

    public static int Solution(int[] food_times, long k) {
        int answer = 1;
        int[] sorted_ft = food_times.clone();
        Arrays.sort(sorted_ft);

        int limit = 0;
        int met = 0;
        int cre = sorted_ft.length;
        // Solution Point 1
        for (int i = 0; i < sorted_ft.length; i += 1) {
            cre = sorted_ft.length - i; // count remain elements
            met = sorted_ft[i];// min eating time
            if (i > 0)
                met -= sorted_ft[i - 1];
            //Checkpoint
            if ((long)cre * met <= k) {
                limit = sorted_ft[i];
                k -= cre * met;
            } else {
                k -= cre * Math.floor(k / cre);
                limit += (int) Math.floor(k / cre);
                break;
            }

        }

        int i = 0;
        boolean flag = true;
        //Solution Point 2
        do {
            if (limit < food_times[i]) {
                food_times[i]--;
                k--;
                answer = i + 1;
                flag = false;
            }

            if (i == food_times.length - 1) {
                i = 0;
                if (flag)
                    return -1;
                flag = true;
            } else
                i++;
        } while (k >= 0);


        return answer;
    }

}
