### Python TMI 정리

- [자료구조](#자료구조)
  - [Set](#Set)
- [연산자](#연산자)

## 자료구조

---

### Set

```python
coex = set(lost) & set(reserve)
lost = list(set(lost)-set(coex))
reserve = list(set(reserve)-set(coex))
```

Mostuse method

```
add /discard/ intersect/ difference
```

& : 교집합

| : 합집합

-: 차집합

+: 이건 합집합 연산을 하지 않는다

## 연산자
