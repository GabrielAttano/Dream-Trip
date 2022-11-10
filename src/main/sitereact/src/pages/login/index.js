import React from 'react';

import { Container } from '../../styles/GlobalStyles';
import { Title, Paragrafo } from './styled';

function Login() {
  return (
    <>
      <Title>DREAMTRIP.COM</Title>
      <Container>
        <Paragrafo>Lorem ipsum dolor sit amet.</Paragrafo>
        <a href="http://google.com">Oie</a>
      </Container>
    </>
  );
}

export default Login;
