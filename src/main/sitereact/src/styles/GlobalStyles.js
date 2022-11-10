import styled, { createGlobalStyle } from 'styled-components';
import { white } from '../config/colors';

export default createGlobalStyle`
  background-color: ${white};

  * {
    margin: 0;
    padding: 0;
    outline: none;
    box-sizing: border-box;
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
`;

export const Container = styled.section`
  /* max-width: 360px; */
  background: black;
  margin: 30px auto;
  padding: 0px 0px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
`;
