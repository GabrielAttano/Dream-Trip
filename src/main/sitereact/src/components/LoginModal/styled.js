import styled from 'styled-components';
import * as Colors from '../../config/colors';

export const Modal = styled.div`
  /* display: ${(props) => (props.showModal ? 'none' : 'block')}; */
  display: ${(props) => (props.isVisible ? 'block' : 'none')};
  position: fixed;
  z-index: 1;
  padding-top: 100px;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: ${Colors.gray750};
`;

export const ModalContent = styled.div`
  background-color: ${Colors.white};
  margin: auto;
  padding-left: 30px;
  box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;
`;
