#!/usr/bin/node
//  Function that compute the number of occurrences of an element in a list.

exports.nbOccurences = function (list, searchElement) {
  const reducer = (total, num) => num === searchElement ? ++total : total;
  return list.reduce(reducer, 0);
};
