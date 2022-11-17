import React from 'react';
import PropTypes from 'prop-types';
import { useSelector, useDispatch } from 'react-redux';
import { FaTimes } from 'react-icons/fa';

import {
  Modal,
  ModalContent,
  TextContainer,
  HrContainer,
  Button,
  ButtonContainer,
  LinkContainer,
} from './styled';

function UserModal({ showModal, closeModal }) {
  const username = useSelector((state) => state.username);
  const dispatch = useDispatch();

  const logout = () => {
    dispatch({
      type: 'LOGOUT_REQUEST',
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
          OLÁ {username.toUpperCase()}, <br />
          QUE BOM TER VOCÊ DE VOLTA!
        </TextContainer>
        <LinkContainer>
          <text>Meus dados</text>
          <text>Meus pedidos</text>
          <text>Meus cartões</text>
        </LinkContainer>
        <HrContainer>
          <hr />
        </HrContainer>
        <LinkContainer>
          <Button onClick={logout} type="button">
            Sair
          </Button>
        </LinkContainer>
      </ModalContent>
    </Modal>
  );
}

UserModal.defaultProps = {
  showModal: false,
};

UserModal.propTypes = {
  showModal: PropTypes.bool,
  closeModal: PropTypes.func.isRequired,
};

export default UserModal;
