#!/usr/bin/node
// Module that exports a Callback to call a function with a parameter plus 1.
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
