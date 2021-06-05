## 변수

#### Integer.parseInt(str)

> str을 정수로 변환



#### String.valueOf(int)

> int 변수를 String 으로 변환





### 배열

#### []

- `int[] score = new int[5];` 혹은 `int[] score = {10, 20, 30, 40, 50};` 처럼 사전에 초기화 가능
- 길이는 `score.length`
- `String[] names = new String(2);`



#### 이차원 배열

- 무조건 `int [][] arr;` 형태여야 한다

- 초기화 : `int [][] arr = new int[4][4];`



#### ArrayList

- `ArrayList<Integer> scoreList = new ArrayList<Integer>;`

```java
ArrayList<Integer> scoreList = new ArrayList<>;
scoreList.add(10);	// add 로 원소 추가
scoreList.add(20);
scoreList.add(30);
scoreList.add(40);

scoreList.add(index 2, element 200);	// 원하는 위치에 추가 가능 
scoreList.remove(index 2);	// 원하는 위치에 제거 가능
System.out.print(scoreList.size);	// 배열 size
System.our.print(scoreList.get(index 0));	// 배열 내 index에 해당하는 원소 출력
```



### 문자열

#### == vs equals()

> 공통점은 양 쪽에 있는 내용을 비교한 값을 boolean type으로 반환한다는 점
>
> 차이점은 아래와 같다

- == 는 연산자, equals() 는 메소드
- == 는 비교고자 하는 대상의 주소값을 비교, equlas 는 대상의 내용 자체를 비교



### Math

- Math.abs()
- Math.floor()
- Math.ceil()
- Math.round()
- Math.max(,)
- Math.min(,)
- Math.pow(,)
- Math.sqrt()



### 기타 주의사항

- char 과 String 의 구분을 확실히 해야한다 -> "" 와 '' 정확히 
- 배열 선언 시, [] 혹은 [] [] 잊지말고 하자
- 
