import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { FaTimes } from 'react-icons/fa';
import PropTypes from 'prop-types';
import LabeledInput from '../Input';
import {
  Modal,
  ModalContent,
  ButtonContainer,
  Button,
  FormContainer,
  TextContainer,
  ContinueButton,
  ContinueButtonContainer,
} from './styled';

function LoginModal({ showModal, closeModal }) {
  const dispatch = useDispatch();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(`Login request ${username} ${password}`);
    dispatch({
      type: 'LOGIN_REQUEST',
      payload: username,
    });
  };

  return (
    <Modal isVisible={showModal}>
      <ModalContent>
        <ButtonContainer>
          <Button type="button" onClick={closeModal}>
            <FaTimes size={20} opacity={0.6} />
          </Button>
        </ButtonContainer>
        <TextContainer>
          OLÁ, <br />
          QUE BOM TER VOCÊ DE VOLTA! <br />
        </TextContainer>
        <FormContainer action="#" className="form" onSubmit={handleSubmit}>
          <LabeledInput
            label="Usuário"
            value={username}
            handleChange={handleUsernameChange}
          />
          <LabeledInput
            label="Senha"
            value={password}
            type="password"
            handleChange={handlePasswordChange}
          />
          <ContinueButtonContainer>
            <ContinueButton type="submit" onClick={handleSubmit}>
              Entrar
            </ContinueButton>
          </ContinueButtonContainer>
        </FormContainer>
        <br />
      </ModalContent>
    </Modal>
  );
}

LoginModal.defaultProps = {
  showModal: false,
};

LoginModal.propTypes = {
  showModal: PropTypes.bool,
  closeModal: PropTypes.func.isRequired,
};

export default LoginModal;
