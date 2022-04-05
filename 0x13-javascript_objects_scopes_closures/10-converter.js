#!/usr/bin/node
exports.converter = function (base) {
  function converts (c) {
    return c.toString(base);
  }
  return converts;
};
