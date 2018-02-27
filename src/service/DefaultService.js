'use strict';


/**
 * recalculate the data utility based on the application
 * By passing the DataUtility values and the application it returns new DataUtility values depending on the application
 *
 * datautility RefinementRequest data utility values
 * returns DataUtility
 **/
exports.refinement = function(datautility) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "timeliness" : 0.1,
  "accuracy" : 0.1,
  "completeness" : 0.1,
  "consistency" : 0.1,
  "URL" : "http://mydatasource/pippo"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}

