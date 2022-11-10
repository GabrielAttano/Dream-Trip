import styled from 'styled-components';
import { black, white } from '../../config/colors';

export const Button = styled.button`
  background-color: ${(props) =>
    props.buttonColor ? props.buttonColor : black};
  color: ${(props) => (props.textColor ? props.textColor : white)};
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 4px;
  width: 208px;
  height: 64px;
  border: 1.5px solid black;
`;
