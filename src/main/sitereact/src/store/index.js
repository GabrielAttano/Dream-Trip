import { legacy_createStore as createStore } from 'redux';

const initialState = {
  showModal: false,
};

const reducer = (action, state = initialState) => {
  const newState = { ...initialState };
  switch (action.type) {
    case 'SHOW_MODAL':
      newState.showModal = !newState.showModal;
      return newState;
    default:
      return state;
  }
};

const store = createStore(reducer);

export default store;
