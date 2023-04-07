package coding_test.wanted;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class A {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] rocks = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            if(Integer.parseInt(st.nextToken()) == 1) rocks[i] = -1;
            else rocks[i] = 1;
        }
        int i=0;
        int j=0;
        int qc = rocks[0];
        while( i < n){
            //ji 조정
            if(qc > 0 && )
        }
        

        
    }

}

/*
 * 예시
9
1 1 1 2 1 1 1 2 1
 -> 5

 1 1 1 2 2 1 1 2 1
 -> 3

10
1 1 1 1 2 2 2 2 1 1
-> 4

5
2 1 1 1 2
-> 3

* 
 */

 /*/
 
 
 
시간 제한	메모리 제한
2 초	512 MB
문제
신을 모시는 사당에는 신을 조각한 돌상 N개가 일렬로 놓여 있다. 각 돌상은 왼쪽 또는 오른쪽을 바라보고 서있다. 창영이는 연속한 몇 개의 돌상에 금칠을 하여 궁극의 깨달음을 얻고자 한다.

궁극의 깨달음을 얻기 위해서는 가능한 한 많은 금색 돌상들이 같은 방향을 바라보아야 한다. 방향이 다른 돌상은 깨달음에 치명적이다. 깨달음의 양은 아래와 같이 정의된다.

| (왼쪽을 바라보는 금색 돌상의 개수) - (오른쪽을 바라보는 금색 돌상의 개수) |

창영이는 궁극의 깨달음을 얻을 수 있을까?

입력
첫째 줄에 돌상의 개수 N이 주어진다.

둘째 줄에 돌상이 나열된 순서대로, 각 돌상이 바라보고 있는 방향이 주어진다. 입력의 편의상 왼쪽은 1, 오른쪽은 2라고 하자.

출력
최대한 많은 깨달음을 얻기 위해 금을 칠하였을 때, 얻을 수 있는 깨달음의 양을 출력한다.

 */