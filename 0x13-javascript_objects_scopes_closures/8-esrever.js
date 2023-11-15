#!/usr/bin/node

exports.esrever = function (list) {
  const rList = [];
  for (const element of list) {
    rList.unshift(element);
  }
  return rList;
};
