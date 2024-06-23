# React Outline
[참고 강의](https://www.inflearn.com/course/lecture?courseSlug=%EC%B2%98%EC%9D%8C-%EB%A7%8C%EB%82%9C-%EB%A6%AC%EC%95%A1%ED%8A%B8)

[공식 문서 Quick Start](https://react.dev/learn)
## 리액트의 장점
- 빠른 렌더링과 업데이트 속도
  - Virtual DOM(Document Object Model) 사용을 통해 업데이트하는 부분을 최소화함으로써 빠른 업데이트
- 컴포넌트 기반
  - 컴포넌트들을 사용하여 빠르고 효율적인 개발이 가능해지고 코드의 재사용성이 올라감
- 커뮤니티가 활발함

## 리액트의 단점
- 높은 상태관리 복잡도
  - Virtual DOM을 사용하면서 State 복잡도가 증가하여 Redux 등 외부 상태관리 라이브러리가 필요함

## JSX
JSX : JavaScript + extention to XML / HTML
```jsx
const element = <h1>Hello, world!</h1>;
```

### createElement
```js
React.createElement(
  type,
  [props],
  [...children]
)
```
- jsx는 사용 시 자동으로 react의 createElement를 호출
### JSX의 장점
- 가독성이 늘어나고 코드 길이가 짧아짐
- Injection Attacks 방어
  - Injection Attack: 텍스트 입력 등에 코드를 입력하는 공격 방식
  - React DOM은 {} 형태로 JSX로 입력받은 값을 자동으로 문자열로 변환하기에 이러한 공격을 막을 수 있음

## Elements
Element: 리액트 앱을 구성하는 가장 작은 블록
DOM Elements: HTML을 구성하는 요소들
React Elements: Virtual DOM에 존재하는 요소들로, 이를 브라우저에 렌더링하면서 DOM Elements로 나타나게 됨
- React Element는 자바스크립트 객체 형태로 존재하며 불변성을 가짐
```js
{
  type: 'button',
  props: {
    className: 'bg-green',
    children: {
      type: 'b',
      props: {
        children: 'Hello, Element!'
      }
    }
  }
}
```
- React Element(JSON 형태)
```js
<button class='bg-green'>
  <b>
    Hello, Element!
  </b>
</button>
```
- DOM Element로 렌더링 된 모습

### createElement
```js
React.createElement(
  type,
  [props],
  [...children]
)
```
- type: HTML 태그
- props: 속성
- children: 해당 엘리먼트의 자식 엘리먼트

### React element의 특징
#### Immutable
불변성: 한 번 생성된 엘리먼트의 children이나 attributes를 바꿀 수 없음

### Element rendering
```js
// index.js

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Library />
  </React.StrictMode>
);
```

## Components and Props
컴포넌트는 JS 함수처럼 입력(Props)를 받아 출력(React element)을 반환함
- 리액트의 컴포넌트는 클래스와 유사하게 기능(Element와 Instance가 유사한 기능으로 동작)

Property(Prop): React component의 속성
- 컴포넌트에 전달할 정보를 담고 있는 JS 객체

### Props의 특징
- Read-Only: 값을 변경할 수 없음
  - 값을 변경하려면 새로운 값을 Element에 전달하여 새로운 Element를 생성해야 함

함수의 순수성(Pure): 같은 입력값에 대해 항상 같은 출력값을 나타냄
- 순수하지 않은 함수
```js
function withdraw(account, amount) {
  account.total -= amount;
}
```
- Impure한 함수 : 입력값을 변경함
- 모든 래익트 컴포넌트는 Props를 직접 바꿀 수 없고 같은 Props에 대해서는 항상 같은 결과를 나타내야 함

```js
// jsx
function App(props) {
  return (
    <Profile 
      width={2500}
      height={1440}
      header={
        <Header title="프로필입니다" />
      }
    />
  );
}
```
```js
function App(props) {
  return React.createElement(
    Profile,
    {
      width: 2500
      height: 1440
      header = React.createElement(Header, { title: "프로필입니다"})
    },
  )
}
```
- JSX 사용이 권장됨

### Component
리액트는 초기에는 Class Component 위주로 사용되었지만, 시간이 흐르면서 Function Component 위주로 바뀌었고 훅을 주로 사용하게 됨

#### Function Component
위에 있는 코드들과 같은 function으로 이루어진 코드

#### Class Component
```js
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```
#### Component Naming
컴포넌트 이름은 항상 대문자로 시작해야 함
- 소문자 컴포넌트는 내장 컴포넌트(태그)로 인식되어 DOM에 전달됨
```const element = <div />;```
- HTML div 태그로 인식됨
```const element = <Welcome name="환영" />;```
- Welcome 리액트 컴포넌트로 인식됨
- 소문자 컴포넌트를 사용하기 위해서는 대문자 변수에 소문자 컴포넌트를 할당한 뒤 해당 변수를 이용하여 사용할 수 있음

#### Component 합성과 추출
컴포넌트 추출: 큰 컴포넌트를 작은 컴포넌트들로 조각내는 것(리팩토링)
```js
function Comment(props) {
  return (
    <div className="comment">
      <div className="user-info">
        <img className="avatar"
          src={props.author.avatarUrl}
          alt={props.author.name}
        />
        <div className="user-info-name">
          {props.author.name}
        </div>
      </div>
      <div className="comment-text">
        {props.text}
      </div>
      <div className="comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}
```
1. avatar 추출
```js
function Avatar(props) {
  return (
    <img className="avatar"
      src={props.user.avatarUrl}
      alt={props.user.name}
    />
  );
}
```
2. UserInfo 추출
```js
function UserInfo(props) {
  return (
    <div className="user-info">
      <Avatar user={props.user} />
      <div className="user-info-name">
        {props.user.name}
      </div>
    </div>
  )
}
```
3. 전체 코드에 반영
```js
function Avatar(props) {
  return (
    <img className="avatar"
      src={props.user.avatarUrl}
      alt={props.user.name}
    />
  );
}

function UserInfo(props) {
  return (
    <div className="user-info">
      <Avatar user={props.user} />
      <div className="user-info-name">
        {props.user.name}
      </div>
    </div>
  )
}

function Comment(props) {
  return (
    <div className="comment">
      <UserInfo user={props.author} />
      <div className="comment-text">
        {props.text}
      </div>
      <div className="comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}
```
## Events and State
State(상태): 리액트 컴포넌트의 변경 가능한 데이터(자바스크립트 객체)로 개발자에 의해 정의됨
- 렌더링, 데이터 흐름에 사용되는 값만 state에 포함되어야 함
- state 변경 시 setState를 통해 수정해야 함
Lifecycle(생명주기): 리액트 컴포넌트마다 가진 생성 시점과 사라지는 시점
- Lifecycle method: 각 컴포넌트가 생성(Mounting), 동작(Updating), 제거(Unmounting)되는 동안 각각의 과정에 사용되는 메서드
  - componentDidMount, componentDidUpdate, componentWillUnmount 함수가 각각의 경우의 commit phase에 사용됨

클릭 이벤트에 따른 state 변화 반영 예시
```js
import { useState } from "react";

export default function UpdateScreen() {
  return (
    <div>
      <h1>두 개의 카운터는 각자 업데이트됩니다.</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
      Clicked {count} times!
    </button>
  );
}
```

## Hooks
Function Component: state를 쓸 수 없고, Lifecycle에 따른 기능을 구현할 수 없음

Hooks: 함수 실행에 맞춰 state / Lifecycle / 최적화 등을 위해 동시에 함수를 실행시키는 함수
- useState: state를 사용하기 위한 Hook
  - ```const [변수명, set함수명] = useState(초기값);```

- useEffect: side effect를 사용하기 위한 Hook
  - side effect: 효과 / 영향(서버에서 데이터를 받아오거나 수동으로 DOM을 변경하는 등 다른 컴포넌트에 영향을 미칠 수 있고 렌더링 중에 완료될 수 없는 작업들)
  - 생명 주기 메서드 3개와 동일한 기능을 수행
  - ```useEffect(이펙트 함수, 의존성 배열);```

- useMemo: Memoization을 위해 사용되는 Hook
```js
import { useMemo } from 'react';

function TodoList({ todos, tab }) {
  const visibleTodos = useMemo(
    () => filterTodos(todos, tab),
    [todos, tab]
  );
  // ...
}
```
  - 연산량이 높은 작업을 수행하여 결과를 반환
  - 렌더링이 일어나는 동안 실행되므로 사이드이펙트는 useMemo가 아닌 useEffect를 사용해야함
  - 의존성 배열을 넣지 않으면 매 렌더링 시마다 실행됨
  - 의존성 배열이 빈 배열인 경우 컴포넌트 마운트 시에만 실행됨

- useCallBack: useMemo와 유사하지만 함수를 반환하는 Hook
```js
import { useCallback } from 'react';

export default function ProductPage({ productId, referrer, theme }) {
  const handleSubmit = useCallback((orderDetails) => {
    post('/product/' + productId + '/buy', {
      referrer,
      orderDetails,
    });
  }, [productId, referrer]);
```
  - 특정 변수가 변한 경우에만 함수를 다시 정의해 주는 역할

- useRef: 레퍼런스(특정 컴포넌트에 접근할 수 있는 객체)를 사용하게 해주는 hook
```js
import { useRef } from 'react';

function MyComponent() {
  const intervalRef = useRef(0);
  const inputRef = useRef(null);
  // ...
```
  - useRef() 사용 시 일부 정보를 기억하면서 렌더링이 일어나지 않도록 함
  - useRef는 내부 데이터가 변경되었을 때 별도로 알림이 발생하지 않음
  - Callback ref: useRef 대신 useCallback을 활용하여 컴포넌트 변경 시 업데이트를 진행되도록 할 수 있음