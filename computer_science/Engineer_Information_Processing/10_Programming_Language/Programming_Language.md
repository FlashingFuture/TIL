# 10. 프로그래밍 언어 활용
## 123. Java의 클래스
```java
class ClassA {
  int a = 10;
  int funcAdd(int x, int y) {
    return x + y + a;
  }
}
public class Test
{
  public static void main(String[] args) {
    int x = 3, y = 6, r;
    ClassA cal = new ClassA();
    r = cal.funcAdd(x, y);
    System.out.println("\n");
    System.out.print(r);
  }
}
```
