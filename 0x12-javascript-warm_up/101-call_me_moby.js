#!/usr/bin/node
// Callback to call a function x times.
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
