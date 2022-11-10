import React from 'react';
import PropTypes from 'prop-types';
import { black, white } from '../../config/colors';
import { Button } from './styled';

function SecondaryButton({ buttonText, buttonColor, textColor }) {
  return (
    <Button buttonColor={buttonColor} textColor={textColor}>
      {buttonText}
    </Button>
  );
}

SecondaryButton.defaultProps = {
  buttonText: 'secondaryButton',
  buttonColor: black,
  textColor: white,
};

SecondaryButton.propTypes = {
  buttonText: PropTypes.string,
  buttonColor: PropTypes.string,
  textColor: PropTypes.string,
};

export default SecondaryButton;
