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