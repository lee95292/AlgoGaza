구종만 저, Algorithm Problem Solving Stratages (인사이트) 

2019 -2 책 씹어먹기 프로젝트


# Chapter 02. 문제 해결과정

1. 문제를 이해하기
2. 문제를 익숙한 용어로 재정의하기
3. 어떻게 해결할지 계획을 세우기
4. 계획을 검증하기
5. 프로그램으로 구현하기
6. 어떻게 풀었는지 돌아보고, 개선할 방법 찾아보기

사실 위 과정은 알고리즘 문제를 한문제라도 풀어봤다면, 너무나도 당연한 과정이다. (6번 돌아보기 과정을 제외하면)

필자는 **각각의 과정에서 주의해야할 부분들**을 설명하고 있다. 

---

* 문제를 이해할 때, 빨리 이해하기 위해 잘못 읽거나 이해하고싶은대로 이해하지 않기
* 계획을 세울 때, 막혀있는 길에서 너무 오래 고민하지 않기
* 계획을 수립하고 검증하는 과정을 건너뛰지 않기
* 회고하는 과정은 항상 중요함. 한번에 정답을 맞추지 못한 경우, 오답노트 등을 작성해서 어떻게 생각했는지 회고해보기

> 위에서 소개한 문제 해결 과정은, 사실 3. 문제 해결을 계획하는 과정과, 5. 프로그램으로 구현하는 과정이 대부분을  차지한다.

> 이 중, 3번 과정에서 문제를 해결할 계획을 세우는 과정을 살펴보자.

1. 비슷한 문제 풀어본 경험 생각해보기. (같은 경로찾기 문제이더라도, 여러 제약조건이 있을 수 있다. 문제의 핵심을 이해한다면, 단순한 변형 문제를 푸는 것을 넘어설 수 있다.
2. 해결한 경험이 없는 종류의 문제라면, 가장 단순한 방법부터 생각해나간다. 가장 간단한 방법부터 시도해보고, 시간/공간적 제약을 최소화시키는 방법을 고민해본다. 점진적인 개선방안을 찾아본다.

3. 문제 해결과정을 수식화 한다.
4. 문제를 단순화한다. 문제를 축소하거나(Bottom - up), 문제를 일반화한다(Generalize) 
5. 그림으로 그려본다
6. 문제 풀이순서를 뒤집거나, 강제한다. (순서를 강제하는 케이스의 경우, p.37의 예제가 상당히 괜찮은듯 하다.)
7. 문제를 정규화한다. ( 사실 이부분은 잘 와닿지 않는다.)


# Chapter 03. 코딩과 디버깅에 관하여

**간결하고 읽기 쉬운 코드**

디자인패턴, 코딩 컨벤션,OOP의 SOLID 원칙 등에서 입이 마르도록 강조하는 것은, 읽고 수정하기 쉬운 코드이다. SOLID원칙에서는 확장성이나 수정 용이성 등 , 여러가지 개념을 포괄적으로 포함하고 있지만, 위의 것들이 공통적으로 강조하는 것을 한 단어로 표현해 본다면, "우아한 코드"이다.

> 3절에서는 우아한 코드를 작성하고, 그것을 잘 활용하기 위한 방법을 알려준다.

1. 간결한 코드 작성하기 - Solid에서 SRP(Single Responsibility Principle)과 매칭된다. 물론 알고리즘 솔빙이 OOP와 크게 상관은 없지만, 하나의 클래스를 작성할 때, 하나의 함수가 한 개의 기능을 가질 수 있도록 하여  재사용성/가독성을 높혀준다.

2.적극적으로 코드 재사용하기 - 코드를 모듈화하여 응집성을 높이는 것은, 간결한 코드 작성과도 관련이 있으며, 코드의 재사용성에도 크게 영향을 미친다. 이는 디버깅 시간을 극적으로 줄여주며, 가독성 역시 향상시키는 방법이다. ~~(한 떄, 함수로 모든 동작을 분리시키면 호출 오버헤드가 발생하지 않을까? 라는 생각을 했지만, 컴파일러 옵션만 잘 주면 해결되는 문제이다.)~~

3. 표준 라이브러리 공부하기- 표준 라이브러리를 통해 제공되는 스택,큐,정렬 등에 대한 소스코드는, 그 개념을 명확히 알고있어야 하지만, 직접 구현하는 일은 없어야 한다.

4. 같은 형태로 프로그램을 작성하기- **검증된 소스코드**를 활용하므로써, 매번 다른 스타일을 적용하는 것에 시간을 쓰지 말자. (물론 알고리즘을 빠르게 풀 때 해당하는 이야기이다.) 이는, 도구가 아니라 내가 풀어야 할 문제에 집중하게 해준다. 

5. 일관적이고 명료한 명명법 사용하기 - 코딩 컨벤션에 해당하고 당연한 내용이지만, 참 지키기 힘들다. Cammelcase, 의미를 갖는 변수명/ 함수명과 변수명 구분/줄여쓰지 않기 등

6. 코드와 데이터를 분리하기 - enumeration이나 배열 등을 활용해, 데이터를 로직에 붙여넣지 않기. 


우아한 코드와는 반대로, 실수를 범하기 쉬운 코딩 스타일 및 사례를 소개한다.

>> **자주 하는 실수**

* 연산자 우선순위 오용 - 잘 알고있다면 가장 좋지만, 헷갈린다면 괄호를 통해 반드시 우선순위를 명시해주도록 하자(시간이 있다면, 헷갈릴 때마다 찾아보기)
* 변수 초기화 문제 - 테스트케이스별로, 또는 논리 로직 상 초기화를 수행해야 하는데 실수로 빠뜨린 경우 등..


>> **디버깅과 테스팅**

* 필자는, 디버거를  사용하는 것이 프로그래밍 대회에서 하나의 자원을 점유하고 시간을 잡아먹는다고 이야기한다. 사실 알고리즘 대회에서는 간결하고 짧은 프로그램이 제출되므로, 눈으로 검증하는  방법과 함께, 다음의 방법들을 추천한다.

* 단정(assert)문 - 조건이 참일 때 무시하고, 거짓일 때에만 프로그램 오류를 발생시키는 코드 작성
* 단위테스트
* 중간결과 확인
* 테스트 방법으로, **느리지만 구현이 완료된 솔루션의 결과값과 개선된 솔루션의 결과를 비교하는 방법의 테스트**

**실수 자료형의 이해**


# Chapter 04. 알고리즘의 시간 복잡도 분석

알고리즘의 시간 분석은, 반복문의 수행횟수로 측정한다. 반복문이 어떤 형태로 수행되는가에 따라 상대적으로 적은 오버헤드들은 무시할 수 있을정도로, 시간복잡도는 반복문이 지배(Dominate)하고있다고 할 수 있다.


* 선형 시간 알고리즘 - 최적의 해일 경우가 높다. 입력을 한 번씩만 순회해도 결과가 나오는 알고리즘은 대회 문제에서 흔하지 않기 때문.
* 선형 이하 시간 알고리즘 - 정렬이 보장된 상태에서의 탐색과 같이, 대부분 제약조건이 더해진 상태에서 수행하는 알고리즘의 경우 존재한다. 
* 지수 시간 알고리즘 