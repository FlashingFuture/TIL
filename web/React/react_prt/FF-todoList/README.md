# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## 개발 일지
- 구조 제작
|--App.jsx
    |
    |--TodoForm.jsx
    |
    |--TodoList.jsx  
        |
        TodoItem.jsx

- 컴포넌트 생성 초기값을 넣어준 후 스타일 적용
- createTodo 기능 제작
- deleteTodo 기능 제작
- 로컬스토리지를 통해 저장 기능 추가
  - useEffect가 생각대로 동작하지 않음: useEffect를 두 개 사용하다 보니 초기조건(Vue로 따지만 onMounted)로 동작하게 한 useEffect 동작 중 todos에 관한 useEffect가 동작해 제대로 로컬스토리지에서 불러오지를 못했음
  - 변수 isOnMounted를 만들어서 첫 실행 시에는 todos에 대한 useEffect가 동작하지 못하도록 막으니까 해결된 듯? 훅의 실행 타이밍들(혹은 생명주기)에 대한 공부가 필요함