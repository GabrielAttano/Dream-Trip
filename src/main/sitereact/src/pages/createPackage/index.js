import React from 'react';
import Header from '../../components/Header';
import Footer from '../../components/Footer';
import DestinosSelector from '../../components/DestinosSelect';
import SecondaryButton from '../../components/SecondaryButton';
import { black, white } from '../../config/colors';
import {
  BlackContainer,
  GrayContainer,
  GrayContainerItem,
  GrayContainerItemRight,
  Title,
} from './styled';

function CreatePackage() {
  const options = [
    { name: 'Brasília', value: 'BSB' },
    { name: 'Rio Branco', value: 'RBR' },
    { name: 'Maceió', value: 'MCZ' },
    { name: 'Macapá', value: 'MCP' },
    { name: 'Manaus', value: 'MAO' },
    { name: 'Salvador', value: 'SSA' },
    { name: 'Fortaleza', value: 'FOR' },
    { name: 'Vitória', value: 'VIX' },
    { name: 'Goiânia', value: 'GYN' },
    { name: 'São Luis', value: 'SLZ' },
    { name: 'Cuiabá', value: 'CGB' },
    { name: 'Campo Grande', value: 'CGR' },
    { name: 'Belo Horizonte', value: 'BHZ' },
    { name: 'Belém', value: 'BEL' },
    { name: 'João Pessoa', value: 'JPA' },
    { name: 'Curitiba', value: 'CWB' },
    { name: 'Recife', value: 'REC' },
  ];

  return (
    <>
      <Header />
      <BlackContainer>
        <GrayContainer>
          <GrayContainerItem>
            <Title>PESQUISE O SEU PRÓXIMO EMBARQUE ABAIXO:</Title>
          </GrayContainerItem>
          <GrayContainerItem>
            <DestinosSelector options={options} defaultName="Origem" />
          </GrayContainerItem>
          <GrayContainerItem>
            <DestinosSelector options={options} defaultName="Destino" />
            <DestinosSelector options={options} defaultName="Destino" />
          </GrayContainerItem>
          <GrayContainerItemRight>
            <GrayContainerItem>
              <SecondaryButton
                buttonColor={white}
                textColor={black}
                buttonText="+ Novo destino"
              />
              <SecondaryButton
                buttonColor={black}
                textColor={white}
                buttonText="Criar pacote"
              />
            </GrayContainerItem>
          </GrayContainerItemRight>
        </GrayContainer>
      </BlackContainer>
      <Footer />
    </>
  );
}

export default CreatePackage;
