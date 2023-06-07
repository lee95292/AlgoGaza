# 리포지토리 규칙
문제 카테고리, 번호 달기

다시보면 좋을문제:                         REMIND 달기  
다시 풀면 좋을 문제:                       REDO 달기  
1시간 내에 풀이를 떠올리지 못하거나, 못 푼 문제: RETRY 달기  (1달 뒤에 다시풀기)

# 코딩테스트 Java 사전지식


* Priority Queue 내림차순으로 사용할 때
```java
PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
```

* [정렬기준 설정] Priority Queue 또는 다른 Collection Framework에서 정렬기준 설정

> 리턴값이 음수 또는 0: left와 right 방향 유지
> 리턴값이 양수 :right와 left방향 교체


자바8 이전: comparator 오버라이딩
```java
PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<String>(){

  @Override
  public int compare(String left, String right){
    return left.length - left.length;
  }
})
```
자바8이후: 람다 표현식

```java
PriorityQueue<Integer> pq = new PriorityQueue<>((left, right) -> { left.length - right.length})
```

Algoritm 리마인드

- 최단거리 알고리즘 리뷰
  - 다익스트라
  - 플로이드 와샬(1389)
  - 벨만-포드
- 문자열 알고리즘
 - trie, kmp 리뷰 
- Segment Tree
- LCS, LIS
- Coin DP
- Tree-DP


### 코딩테스트 준비할때
알고리즘 종류별로 많이 풀기 
배 채우기  
코세척 
잠 충분히 자기 



