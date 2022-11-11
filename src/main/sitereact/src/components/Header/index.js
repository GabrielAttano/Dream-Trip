import React from 'react';
import { useDispatch } from 'react-redux';
import { Title, HeaderContainer, LoginContainer } from './styled';
import PrimaryButton from '../PrimaryButton';

function Header() {
  const dispath = useDispatch();
  const handleClick = (e) => {
    e.preventDefault();
    dispath({
      type: 'SHOW_MODAL',
    });
  };

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
