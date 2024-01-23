### 리스트 입력 메서드의 자료구조
```list.append(x)```
- ```a[len(a):] = [x]``` 와 같음

```list.extend(iterable)```
- ```a[len(a):] = iterable``` 과 같음

```list += [x]```
- ```list = iadd(list, [x])``` 와 같음
- 둘을 더해 새로운 리스트를 만드는(BUILD_LIST) 과정이 들어가 append보다 비효율적임
- ```extend```와 ```+=```는 비슷한 속도를 보임

```python
import dis

def list_compare():
    list1 = ['a', 'b', 'c']
    list2 = ['d', 'e', 'f']
    add_char = 'w'
    add_list = ['x', 'y', 'z']

    list1.append(add_char)
    list2 += add_char

    list1.extend(add_list)
    list2 += add_list

    return 0

dis.dis(list_compare)

```