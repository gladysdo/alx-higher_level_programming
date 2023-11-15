#!/usr/bin/node

exports.converter = function (base) {
  return function (numbers) {
    return numbers.toString(base);
  };
};
