import { legacy_createStore as createStore } from 'redux';

const initialState = {
  isLogged: false,
  username: '',
};

// eslint-disable-next-line
const reducer = (state = initialState, action) => {
  if (!action) {
    return state;
  }
  const newState = { ...state };
  switch (action.type) {
    case 'LOGIN_REQUEST':
      newState.isLogged = true;
      newState.username = action.payload;
      return newState;
    case 'LOGOUT_REQUEST':
      newState.isLogged = false;
      newState.username = '';
      return newState;
    default:
      return state;
  }
};

const store = createStore(reducer);

export default store;
