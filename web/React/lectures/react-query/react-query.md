# Data Fetching with Tanstack Query
## Tanstack Query
Tanstack Query : A library that helps with sending HTTP requests and keeping your frontend UI in sync
- useEffect, fetch 등의 기능을 이용해서 구현할 수 있는 기능들
- 훨씬 코드를 단순화할 수 있음
- 캐싱 등 다양한 기능을 쉽게 사용해 앱을 향상시킬수 있음

### Using Tanstack Query
Tanstack Query는 HTTP 요청을 보내는 기능을 가지고 있지 않고, 
데이터, 에러, 캐싱 등을 관리하는 기능을 가짐

#### useQuery
```
  const { data } = useQuery({
    queryKey: ['events',],
    queryFn: fetchEvents
  });
```