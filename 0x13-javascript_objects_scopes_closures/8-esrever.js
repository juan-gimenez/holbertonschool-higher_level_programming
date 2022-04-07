#!/usr/bin/node
// reverse list
exports.esrever = function (list) {
  const reverlist = [];
  if (list === undefined) {
    return;
  } else {
    for (let x = 0; x < list.length; x++) {
      reverlist.unshift(list[x]);
      // add elem
    }
  }
  // reversed list
  return reverlist;
};
