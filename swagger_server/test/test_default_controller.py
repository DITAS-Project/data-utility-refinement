# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.data_utility import DataUtility  # noqa: E501
from swagger_server.models.refinement_request import RefinementRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_refinement(self):
        """Test case for refinement

        recalculate the data utility based on the application
        """
        datautility = RefinementRequest()
        response = self.client.open(
            '/ditas-project/DataUtilityRefinement/0.2.1/datautilityrefinement',
            method='POST',
            data=json.dumps(datautility),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
