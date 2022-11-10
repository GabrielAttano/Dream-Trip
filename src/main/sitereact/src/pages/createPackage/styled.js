import styled from 'styled-components';
import * as Colors from '../../config/colors';

export const BlackContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: ${Colors.black};
  padding: 76px 135px;
`;

export const Title = styled.h1`
  color: ${Colors.white};
  font-size: 24px;
  font-weight: normal;
`;

export const GrayContainer = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  background-color: ${Colors.gray750};
  width: 100%;
  height: 100%;
  border-radius: 4px;
  padding: 32px 48px;
  gap: 48px;
`;

export const GrayContainerItem = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 24px;
`;

export const GrayContainerItemRight = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  width: 100%;
  gap: 24px;
`;

export const Input = styled.input`
  width: 256px;
  height: 64px;
  padding-left: 24px;
  padding-top: 30px;
  color: ${Colors.gray750};
  font-size: 20px;
  border-radius: 4px;
`;
