'use strict';

var utils = require('../utils/writer.js');
var Default = require('../service/DefaultService');

module.exports.refinement = function refinement (req, res, next) {
  var datautility = req.swagger.params['datautility'].value;
  Default.refinement(datautility)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
