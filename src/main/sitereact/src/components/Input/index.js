import React from 'react';
import PropTypes from 'prop-types';

import { Input, InputContainer, Label } from './styled';

function LabeledInput({ label, value, type, handleChange }) {
  return (
    <InputContainer>
      <Input type={type} value={value} onChange={handleChange} />
      <Label>{label}</Label>
    </InputContainer>
  );
}

LabeledInput.defaultProps = {
  type: 'text',
};

LabeledInput.propTypes = {
  label: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  handleChange: PropTypes.func.isRequired,
  type: PropTypes.string,
};

export default LabeledInput;
