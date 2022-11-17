import styled, { createGlobalStyle } from 'styled-components';
import { white } from '../config/colors';
import RobotoWoff from '../fonts/Roboto.woff';
import RobotoWoff2 from '../fonts/Roboto.woff2';

export default createGlobalStyle`
  background-color: ${white};

  * {
    margin: 0;
    padding: 0;
    outline: none;
    box-sizing: border-box;
    font-family: 'Roboto';
  }

  body {
    font-family: sans-serif;
  }

  html, body, #root {
    height: 100%;
  }

  button {
    cursor: pointer;
  }

  a {
    text-decoration: none;
  }

  ul {
    list-style: none;
  }

  @font-face {
    font-family: 'Roboto';
    src: local('Roboto'),
    url(${RobotoWoff2}) format('woff2'),
    url(${RobotoWoff}) format('woff');
    font-weight: 300;
    font-style: normal;
  }
`;

export const Container = styled.section`
  /* max-width: 360px; */
  background: black;
  margin: 30px auto;
  padding: 0px 0px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
`;
