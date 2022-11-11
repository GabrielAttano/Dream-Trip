import React from 'react';
import { useSelector } from 'react-redux';
import { Modal, ModalContent } from './styled';

function LoginModal() {
  const showModal = useSelector((state) => state.showModal);

  return (
    <Modal isVisible={showModal}>
      <ModalContent>
        Hey its io boy skinny
        <br />
        <button type="button">X</button>
      </ModalContent>
    </Modal>
  );
}

export default LoginModal;
