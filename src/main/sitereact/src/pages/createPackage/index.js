import React, { useState } from 'react';
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
  Input,
  Title,
} from './styled';

function CreatePackage() {
  const maxDestinos = 5;
  const minDestinos = 2;
  const [totalDestinos, setTotalDestinos] = useState(minDestinos);
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

  const addDestino = (e) => {
    e.preventDefault();
    if (totalDestinos < maxDestinos) {
      setTotalDestinos(totalDestinos + 1);
    }
  };

  const removeDestino = (e) => {
    e.preventDefault();
    if (totalDestinos > minDestinos) {
      setTotalDestinos(totalDestinos - 1);
    }
  };

  const criaPacote = (e) => {
    e.preventDefault();
    console.log('criando pacote');
  };

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
            <Input type="date" placeholder="Data de partida" />
          </GrayContainerItem>
          <GrayContainerItem>
            {[...Array(totalDestinos)].map(() => (
              <DestinosSelector options={options} defaultName="Destino" />
            ))}
          </GrayContainerItem>
          <GrayContainerItemRight>
            <GrayContainerItem>
              <SecondaryButton
                buttonColor={white}
                textColor={black}
                buttonText="+ Novo destino"
                handleClick={addDestino}
              />
              <SecondaryButton
                buttonColor={white}
                textColor={black}
                buttonText="- Remover destino"
                handleClick={removeDestino}
              />
              <SecondaryButton
                buttonColor={black}
                textColor={white}
                buttonText="Criar pacote"
                handleClick={criaPacote}
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
