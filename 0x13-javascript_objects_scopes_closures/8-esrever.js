#!/usr/bin/node
//  Function that compute the reversed version of a list.

exports.esrever = function (list) {
  const reversed = [];
  for (const i of list) {
    reversed.unshift(i);
  }
  return reversed;
};
