import React from 'react';
import { Router } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './store';
import history from './services/history';
import GlobalStyle from './styles/GlobalStyles';
import Routes from './routes';

function App() {
  return (
    <Provider store={store}>
      <Router history={history}>
        <Routes />
        <GlobalStyle />
      </Router>
    </Provider>
  );
}

export default App;
