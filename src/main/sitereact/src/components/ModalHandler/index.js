import React, { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';
import PropTypes from 'prop-types';

import modalTypes from './ModalTypes';
import LoginModal from '../LoginModal';
import UserModal from '../UserModal';

function ModalHandler({ modal, showModal, closeModal }) {
  const [modalComponent, setModalComponent] = useState(
    <LoginModal showModal={showModal} closeModal={closeModal} />
  );
  const [currentModalType, setCurrentModal] = useState(modal);
  const isLogged = useSelector((state) => state.isLogged);

  const handleChange = (modalType) => {
    switch (modalType) {
      case modalTypes.loginModal:
        setModalComponent(
          <LoginModal showModal={showModal} closeModal={closeModal} />
        );
        break;
      case modalTypes.UserModal:
        setModalComponent(
          <UserModal showModal={showModal} closeModal={closeModal} />
        );
        break;
      default:
        break;
    }
    setCurrentModal(modalType);
  };

  useEffect(() => {
    console.log('show modal change');
    handleChange(currentModalType);
  }, [showModal]);

  useEffect(() => {
    console.log('modal change');
    if (modal !== currentModalType) {
      setCurrentModal(modal);
    }
    handleChange(currentModalType);
  }, [modal]);

  useEffect(() => {
    console.log('is logged change');
    if (isLogged) {
      handleChange(modalTypes.UserModal);
    } else {
      handleChange(modalTypes.loginModal);
    }
  }, [isLogged]);

  return <div className="Modal">{modalComponent}</div>;
}
ModalHandler.defaultProps = {
  modal: modalTypes.loginModal,
};

ModalHandler.propTypes = {
  showModal: PropTypes.bool.isRequired,
  closeModal: PropTypes.func.isRequired,
  modal: PropTypes.string,
};

export default ModalHandler;
