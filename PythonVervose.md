### Python TMI 정리

- [자료구조](#자료구조)
  - [Set](#Set)
- [연산자](#연산자)

## 알고리즘

---

### sort

sorted(정렬할 리스트, 정렬기준 키) :정렬한 결과를 반환, key argument를 통해 정렬할 수 있음

```python
routesOut = sorted(routes, key=lambda route: route[1])
```

## 자료구조

---

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
