import React, { useCallback } from 'react';

import { Title, HeaderContainer, LoginContainer } from './styled';
import PrimaryButton from '../PrimaryButton';

function Header() {
  const handleClick = useCallback(() => {
    console.log();
  });

  return (
    <HeaderContainer>
      <Title>DREAMTRIP.COM</Title>
      <LoginContainer>
        <a href="Ajuda">ajuda</a>
        <PrimaryButton buttonText="Entrar" handleClick={handleClick} />
      </LoginContainer>
    </HeaderContainer>
  );
}

export default Header;
