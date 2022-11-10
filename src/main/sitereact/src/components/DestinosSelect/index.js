import React from 'react';
import PropTypes from 'prop-types';
import { Select } from './styled';

function DestinosSelector({ options, defaultName }) {
  const optionsArr = [...options];
  optionsArr.unshift({ name: defaultName, value: 'none' });

  return (
    <Select>
      {optionsArr.map((option) => (
        <option key={option.value} value={option.value}>
          {option.name}
        </option>
      ))}
    </Select>
  );
}

DestinosSelector.propTypes = {
  options: PropTypes.arrayOf(
    PropTypes.shape({
      name: PropTypes.string.isRequired,
      value: PropTypes.string.isRequired,
    })
  ).isRequired,
  defaultName: PropTypes.string.isRequired,
};

export default DestinosSelector;
