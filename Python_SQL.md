# Python

### 아스키코드

- 대문자 : 65 ~ 90
- 소문자 : 97 ~ 122
- 문자 -> 숫자 `ord()`
- 숫자 -> 문자 `chr()`



### import math

- `math.factorial(숫자)` : 팩토리얼
- `math.sqrt(숫자)` : 제곱근
- `ceil(숫자)` : 올림
- `floor(숫자)` : 내림
- `round(숫자)` : 반올림
- `abs(숫자)` : 절대값



### 출력

- `print("".join(list))` : 괄호 없이 배열 출력
- `arr[::-1]` : 문자열, 배열 반대로 출력
- `reversed(list)` 또는 `list = list.reverse()`



### from itertools import

- `from itertools import combinations`

  - `list = combinations(list, num)`

- `from itertools import permutations`

  - `permutations(list,num)`

- `from itertools import product`

  > 모든 각 리스트에서 1개씩 뽑아서 만들 수 있는 모든 조합의 수

  - `product(arr1, arr2....)` 여러개 가능
  - `product('ABCD', 'xy')` --> Ax Ay Bx By Cx Cy Dx Dy
  - `product(range(2), repeat=3)` --> 000 001 010 011 100 101 110 111
  - `list(map(sum, product(*l)))` : 몇 개 넣을지 모를 때 * 사용



### 힙, 큐, 스택

#### `from collections import deque`

```python
from collections import deque
queue = deque()
queue.append(i) 	
queue.popleft()
list(queue) # 하면 리스트 자료형이 반환
```



#### import heapq

```python
import heapq
h = []
heapq.heappush(h,1)
heapq.heappop(h)
```



### if not arr:

> 리스트가 null 인지 확인할 때



### import sys

> import sys 하고 input = sys.stdin.readline 한 후 평소대로 입력받으면 시간 단축



### for문

- `for index, element in enumerate(arr):`
- `list.index(10)`: 리스트에서 인덱스 추출
- `if any 조건` : 조건에 하나라도 맞으면
  - `for p1, p2 in zip(arr, arr[1:]):`arr에서 요소가 0 1	1 2 	2 3 ... 이런식으로 출력됨



### 딕셔너리

- `dict.get(key_name)` : value 반환
- `dict.keys()` : 전체 키 리스트로 반환
- `del dict[key]` : 키-값 삭제
- `if not h.get(key_name)` : 딕셔너리에서 키 값에 해당하는 값이 없을 때 또는 키가 없을 때
- `h = sorted(h.items, key = lambda x: -x[1])` : 딕셔너리 내림차순으로 정렬



### 정렬

- `arr.sort()` 는 리스트만을 위한 메소드이지만 `sorted()` 함수는 어떤 이터러블 객체도 받을 수 있음



### *

```python
mylist = [[1,2,3],[4,5,6],[7,8,9]]
list(map(list, zip(*mylist)))	
# 결과 :  [[1, 4, 7], # [2, 5, 8], # [3, 6, 9]]
```





# SQL

### LIMIT

> 상위 n개 레코드

```mysql
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1;
```



### IS NULL, DISTINCT

- COUNT 괄호 안에 DISTINCT 있어야 함
- `IS NOT NULL` 과 `IS NULL` 로 널 체크

```mysql
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS WHERE NAME is not NULL;
```



### DATETIME

- TYPE이 DATETIME 인 데이터에서 시간만 추출하려면 HOUR을 사용

```mysql
SELECT HOUR(DATETIME) HOUR, COUNT(DATETIME) COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR(DATETIME)
HAVING HOUR >= 9 and HOUR <= 19
```

#### DATE_FORMAT (date, format) 

- `%m` : 7	`%M` : JULY
- `%d` : 1	`%D `: 1st

```mysql
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, "%Y-%m-%d") AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```



### IFNULL(A, B)

> A가 NULL 이면 B를, 아니면 A 

- NAME IFNULL 이 아니고 바로 IFNULL 임

```mysql
SELECT ANIMAL_TYPE, IFNULL(NAME, "No name") AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```



### (LEFT) JOIN 테이블명 ON 조건

- DATETIME 끼리 뺴기 가능

```mysql
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
FROM ANIMAL_OUTS
LEFT JOIN ANIMAL_INS 
ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
ORDER BY ANIMAL_OUTS.DATETIME - ANIMAL_INS.DATETIME DESC LIMIT 2;
```



### CASE WHEN 조건 THEN 특정값 ELSE 특정값 END AS 컬럼명

- 조건이 여러개일 경우 WHEN 을 END 로 연결하지 않고 각각 WHEN 선언해야함

```mysql
SELECT ANIMAL_ID, NAME,
CASE WHEN SEX_UPON_INTAKE LIKE "Neutered%" THEN "O"
    WHEN SEX_UPON_INTAKE LIKE "Spayed%" THEN "O"
    ELSE "X"
END AS "중성화"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```



### LIKE % _

> 와일드 문자 
>
> % : 0개 이상의 문자열과 대치
>
> _ : 한 개의 문자와 대치

```mysql
WHERE NAME LIKE 'A%'
WHERE ANIMAL_INS.SEX_UPON_INTAKE LIKE '%Intact%' 
```



### IN

- () 사용

```mysql
WHERE NAME IN ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')
```



### SET

>  SET 옆에 변수명과 초기값을 설정

- `@`가 붙은 변수는 프로시저가 종료되어도 유지 ( 이를 통해 값을 누적하여 0부터 23까지 표현 )
- `:=`은 비교 연산자 =과 혼동을 피하기 위한 대입 연산
  - SELECT (@hour := @hour +1) 은 @hour의 값에 1씩 증가시키면서 SELECT 문 전체를 실행
  - 이 때 처음에 @hour 값이 -1 인데, 이 식에 의해 +1 이 되어 0이 저장
  - HOUR 값이 0부터 시작
  - WHERE @hour < 23일 때까지, @hour 값이 계속 + 1씩 증가

```mysql
SET @hour := -1; -- 변수 선언

SELECT (@hour := @hour + 1) as HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23
```

