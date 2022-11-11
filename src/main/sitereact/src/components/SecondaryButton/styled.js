import styled from 'styled-components';

export const Button = styled.button`
  background-color: ${(props) => props.buttonColor};
  color: ${(props) => props.textColor};
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 4px;
  width: 208px;
  height: 64px;
  border: 1.5px solid black;
`;
