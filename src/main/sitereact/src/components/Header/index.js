import React, { useState } from 'react';
import { useSelector } from 'react-redux';

import { Title, HeaderContainer, LoginContainer } from './styled';
import ModalHandler from '../ModalHandler';
import PrimaryButton from '../PrimaryButton';

function Header() {
  const [showModal, setShowModal] = useState(false);
  const isLogged = useSelector((state) => state.isLogged);

  const handleClick = (e) => {
    e.preventDefault();
    setShowModal(true);
  };

  return (
    <HeaderContainer>
      <Title>DREAMTRIP.COM</Title>
      <LoginContainer>
        <a href="Ajuda">ajuda</a>
        {isLogged ? (
          <PrimaryButton buttonText="Perfil" handleClick={handleClick} />
        ) : (
          <PrimaryButton buttonText="Entrar" handleClick={handleClick} />
        )}
        {/* <PrimaryButton buttonText="Entrar" handleClick={handleClick} /> */}
        <ModalHandler
          showModal={showModal}
          closeModal={() => setShowModal(false)}
        />
      </LoginContainer>
    </HeaderContainer>
  );
}

export default Header;
