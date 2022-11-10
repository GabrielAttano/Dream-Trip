import React from 'react';
import { FaRegCircle } from 'react-icons/fa';
import { Title, FooterContainer, HR, LinksContainer } from './styled';

function Footer() {
  return (
    <FooterContainer>
      <div>
        <Title>DREAMTRIP.COM</Title>
      </div>
      <HR />
      <LinksContainer>
        <FaRegCircle size={40} />
        <FaRegCircle size={40} />
        <FaRegCircle size={40} />
        <FaRegCircle size={40} />
      </LinksContainer>
    </FooterContainer>
  );
}

export default Footer;
