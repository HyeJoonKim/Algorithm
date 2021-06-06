## 변수

#### Integer.parseInt(str)

> str을 정수로 변환



#### String.valueOf(int)

> int 변수를 String 으로 변환



### 배열

#### []

- `int[] score = new int[5];` 혹은 `int[] score = {10, 20, 30, 40, 50};` 처럼 사전에 초기화 가능
- 배열 길이는 `score.length`
- `String[] names = new String(2);`
- String 길이는 length()



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
System.out.print(scoreList.size());	// 배열 size
System.our.print(scoreList.get(index 0));	// 배열 내 index에 해당하는 원소 출력
```

- 주로 `List<Integer> ans = new ArrayList<>();` 로 선언하고, 이 때는 `import java.util.ArrayList;` 와 `import java.util.List;` 를 꼭 선언해야 한다.



### 문자열

#### == vs equals()

> 공통점은 양 쪽에 있는 내용을 비교한 값을 boolean type으로 반환한다는 점
>
> 차이점은 아래와 같다

- == 는 연산자, equals() 는 메소드
- == 는 비교고자 하는 대상의 주소값을 비교, equlas 는 대상의 내용 자체를 비교



#### charAt(index)

> String 에서 index 위치에 해당되는 문자 추출하기

```java
String str = "abcde";
char c = str.charAt(0);	// a 가 저장됨
```



#### substring(시작,끝)

> 원하는 범위만큼 문자열 잘라내기



#### split(규칙)

> 주어진 문자로 분리하여 배열에 저장

```java
String str = "a bc def";
String[] data = str.split(" ");	// 띄어쓰기를 구분으로 하여 배열 저장
>> a	bc	def 로 저장됨
```



#### replace

> 문자열 내 특정 문자 제거

``` java
String MyString = "Hello World"; 
MyString = MyString.replace(" ", ""); 
```



#### replaceAll

> replace 와 동일하지만, 정규 표현식을 사용할 수 있음

##### 정규표현식

- `.` : 어떤 문자 1개를 의미
- `[abcd]` : a,b,c,d 중 문자 1개 
- `[^a-z]` : a 부터 z 를 제외한 문자 1개
- `[a-d 1-3]` : a 부터 d, 1 부터 3 사이의 문자 1개
- `x|z` : x 또는 z
- `^blah` : blah 로 시작하는지
- `blah$` : $ 앞의 blah 가 line의 마지막으로 끝나는지 

```java
class Solution {
    public String solution(String new_id) {
        String answer = "";
        String temp = new_id.toLowerCase();
        
        temp = temp.replaceAll("[^a-z0-9-_.]",""); // 소문자, 숫자, 특수문자 제외 제거
        temp = temp.replaceAll("[.]{2,}",".");	// . 이 2번 이상 중복되면 . 으로 치환
        temp = temp.replaceAll("^[.]|[.]$", "");	// .으로 시작하거나 끝나면 제거
        
        if (temp.length()==0)
            temp += 'a';
        if (temp.length()>=16){
            temp = temp.substring(0,15);
            temp = temp.replaceAll("[.]$","");
        }
        if (temp.length() <= 2){
            char c = temp.charAt(temp.length()-1);
            while (temp.length() < 3){
                temp += c;
            }
        }
        
        return temp;
    }
}
```



### 대문자 소문자

#### 대문자를 소문자로, 소문자를 대문자로 모두 변환하기

```java
String str1 = 'hello java';
str1.toUpperCase(); // 모두 대문자로

String str2 = 'HELLO';
str2.toLowerCase();	// 모두 소문자로
```



#### 대소문자 구별

```java
char ch = 'a';
Character.isLowerCase(ch); 	// 소문자인지

char ch1 = 'A';
Character.isUpperCase(ch1); // 대문자인지
```



### Math

- Math.abs()
- Math.floor()
- Math.ceil()
- Math.round()
- Math.max(,)
- Math.min(,)
- Math.pow(,)
- Math.sqrt()



#### 몫 연산

> 나머지 연산은 있지만 // 사용 불가. 나눗셈 후 정수로 casting

```java
(int)s.length()/2
```



### Queue

> 자바에서 큐는 Linked List를 활용하여 생성한다.

```java
import java.util.LinkedList;
import java.util.Queue;

Queue<Integer> q = new LinkedList<>();

q.add(1);	// 추가, 추가 성공하면 true 반환
q.offer(2);	// 추가

q.poll();	// 첫번째 값 반환하고 제거, 비어있다면 null
q.remove(); // 첫번째 값 제거하면서 반환
q.clear();	// 초기화

q.peek();	// 첫번째 값 반환
```



### Stack

```java
import java.util.*;

Stack<T> s = new Stack<>();
```

- push() : 스택에 삽입

- pop() : 스택에서 가장 위에 있는 값 반환하고 없앰

- peek() : 스택에서 가장 위에 있는 값 반환

- isEmpty() : 스택이 비어있는지를 반환

- size() : 스택에 있는 요소의 크기 반환



### Deque

```java
import java.util.*;

Deque<T> deque = new LinkedList<>();
```

- addFirst() : 앞에 요소 삽입
- addLast() : 뒤에 요소 삽입
- peekFirst() : 앞 요소 반환
- peekLast() : 뒤 요소 반환
- pollFirst() : 앞 요소 없애면서 반환
- pollLast() : 뒤 요소 없애면서 반환



### 정렬

```java
import java.util.Arrays;

public class Sort{
    public static void main(String[] args)  {
        int arr[] = {4,23,33,15,17,19};
        Arrays.sort(arr);	// 오름차순 정렬
		Arrays.sort(arr,Collections.reverseOrder()); // 내림차순 정렬
        // 내림차순 구현에는 int[] 가 아니고, Integer[] 써야한다
        Arrays.sort(arr, 0, 4); // 0,1,2,3 요소만 정렬
        
        System.out.println(Arrays.toString(arr)); // 출력은 이런식으로
    }
}
```



### HashMap

```java
HashMap<String, Integer> h = new HashMap<>();

h.put("apple". 1);	// 값 추가
h.putAll(h1);	// 두개 해시맵 합치기
h.get("apple");	// 1 반환
h.remove("apple");	// key에 해당하는 데이터 삭제, 삭제되면서 value 리턴
h.clear(); // 모든 데이터 삭제
h.isEmpty();	// 데이터가 비어있는지 확인

h.keySet();	// 저장된 key들을 set 객체로 리턴
h.values(); // value 들을 Collection 객체로 리턴

h.containsKey("apple");	// apple이 인자인 key가 있으면 true, 없으면 false 반환
h.containsValue(1);	

h.replace("apple", 10);	// key의 value를 교체해준다. 교체되어 삭제되는 value return 해줌
//존재하지 않는 key면 null 리턴
```



### startsWith() / endsWith()

> `boolean startsWith(String)` 대상 문자열이 특정 문자 혹은 문자열로 시작하는지 체크
>
> true / false 값을 리턴한다

```java
String a = "java";
a.startsWith("j");	//true
a.endsWitn("a");	//true
```

- 공백도 인식하므로 주의



### Iterator 반복자

```java
Iterator<String> it = list.iterator();

while(it.hasNext()){
    answer *= it.next().intValue();
}
```





### 기타 주의사항

- char 과 String 의 구분을 확실히 해야한다 -> "" 와 '' 정확히 
- 배열 선언 시, [] 혹은 [] [] 잊지말고 하자
- 
