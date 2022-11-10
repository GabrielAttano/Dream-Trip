import React from 'react';
import PropTypes from 'prop-types';

import { Button } from './styled';

function PrimaryButton({ buttonText, handleClick }) {
  return <Button onClick={handleClick}>{buttonText}</Button>;
}

PrimaryButton.defaultProps = {
  buttonText: 'PrimaryButton',
};

PrimaryButton.propTypes = {
  buttonText: PropTypes.string,
  handleClick: PropTypes.func.isRequired,
};

export default PrimaryButton;
