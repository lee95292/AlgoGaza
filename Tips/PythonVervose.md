### Python TMI 정리

- [자료구조](#자료구조)
  - [Set](#Set)
- [연산자](#연산자)

- [입력](#입력)

## 알고리즘

---

### sort

sorted(정렬할 리스트, 정렬기준 키) :정렬한 결과를 반환, key argument를 통해 정렬할 수 있음

```python
routesOut = sorted(routes, key=lambda route: route[1])
```

## 자료구조

---

### List

List to String

```pythton
mylsit=['22','424','ab']
''.join(mylist)
```

### Set

```python
coex = set(lost) & set(reserve)
lost = list(set(lost)-set(coex))
reserve = list(set(reserve)-set(coex))
```

Most use method

```
add /discard/ intersect/ difference
```

& : 교집합

| : 합집합

-: 차집합

+: 이건 합집합 연산을 하지 않는다

## 연산자

## 기타

```python
sys.setrecursionlimit(10**6)
```

파이썬 기본 재귀함수 콜스택은 1000. >> 재귀를 이용해 문제를 풀려면 설정해주자.
