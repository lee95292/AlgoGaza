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

Algoritm Todo

- 최단거리 알고리즘 리뷰
  - 다익스트라
  - 플로이드 와샬(1389)
  - 벨만-포드
- 문자열 알고리즘
 - trie, kmp 리뷰 
- 세그먼트 트리 알고리즘 공부

다시 풀어볼 문제
7662(이중 우선순위 큐) 
13549, 순간이동  우선순위 큐로 풀기


