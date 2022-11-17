import styled from 'styled-components';
import * as Colors from '../../config/colors';

export const InputContainer = styled.div`
  position: relative;
  display: flex;
  flex-direction: column;
`;

export const Label = styled.label`
  position: absolute;
  pointer-events: none;
  transform: translate(0, 23px) scale(1);
  transform-origin: top left;
  transition: 200ms cubic-bezier(0, 0, 0.2, 1) 0ms;
  color: ${Colors.black};
  font-size: 12px;
  line-height: 1;
  left: 16px;
  input:focus ~ & {
    transform: translate(0, 12px) scale(0.8);
    color: ${Colors.gray50};
  }
`;

export const Input = styled.input`
  width: 272px;
  height: 64px;
  padding-left: 25px;
  padding-top: 28px;
  color: ${Colors.black};
  font-size: 20px;
  border-radius: 4px;
`;
